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
