'''
given an array, for each possible window of size k, whats the biggest smallest element ?
'''

def compute_next_elem(arr, indexes, v):
    s = [] # inc val stack
    for i in indexes:
        # while current elem is smaller than top of stack
        # s[-1] is index of the largest elem in stack
        while len(s) > 0 and arr[s[-1]] >= arr[i]:
            s.pop(-1)
        if len(s) > 0:
            v[i] = s[-1]
        # put current elem index on top of stack
        s.append(i)
    return v

def max_min_window(arr):
    n = len(arr)
    # find indexes of next/previous smaller for i-th element
    left = compute_next_elem(arr, range(n), [-1 for _ in range(n+1)])
    right = compute_next_elem(arr, range(n-1, -1, -1), [n for _ in range(n+1)])
    # arr:   [1,  2, 3, 5, 1,  7, 3]
    # left:  [-1, 0, 1, 2, -1, 4, 4, -1]
    # right: [7,  4, 4, 4, 7,  6, 7, 7]

    ans = {}
    for i in range(n):
        # length of the window
        l = right[i] - left[i] - 1
        # where arr[i] is minimum for ans[i]
        ans[l] = max(ans.get(l,0), arr[i])

    for i in range(n-1, -1, -1):
        ans[i] = max(ans.get(i,0), ans.get(i+1,0))
    return ans

print(max_min_window([1,2,3,5,1,7,3]))
# ans: {7: 1, 3: 2, 2: 3, 1: 7, 6: 1, 5: 1, 4: 1, 0: 7}
