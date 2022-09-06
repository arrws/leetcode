def binary_search(v, x):
    # v sorted
    l, r = 0, len(v)-1
    while l <= r:
        m = int((l+r)/2)
        if v[m] == x:
            print(m)
            return
        elif v[m] < x:
            l = m+1
        else:
            r = m-1
    print(-1)

binary_search([2,3,4,10,40], 10)

def peak_elem(arr) -> int:
    i, j = 0, len(arr) - 1
    while i < j:
        # print(arr[i:j])
        m = (i + j) // 2
        if arr[m] > arr[m+1]:
            j = m
        else:
            i = m+1
    return i
