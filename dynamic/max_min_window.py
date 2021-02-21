def max_min_window(a):
    # for each possible window of size k whats the biggest smallest element ?
    n = len(a)
    # find indexes of next/previos smaller of each element
    left = [-1 for _ in range(n+1)]
    right = [n for _ in range(n+1)]

    s = []
    for i in range(n):
        while len(s) > 0 and a[s[-1]] >= a[i]:
            s.pop(-1)
        if len(s) > 0:
            left[i] = s[-1]
        s.append(i)

    s = []
    for i in range(n-1, -1, -1):
        while len(s) > 0 and a[s[-1]] >= a[i]:
            s.pop(-1)
        if len(s) > 0:
            right[i] = s[-1]
        s.append(i)
    print(a)
    print(left)
    print(right)

    # where a[i] is minimum for ans[i]
    ans = {}
    for i in range(n):
        # length of the window
        l = right[i] - left[i] - 1
        ans[l] = max(ans.get(l,0), a[i])

    print(ans)
    for i in range(n-1, -1, -1):
        ans[i] = max(ans.get(i,0), ans.get(i+1,0))
    print(ans)


max_min_window([1,2,3,5,1,7,3])

