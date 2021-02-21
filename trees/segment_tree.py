a = [0 for _ in range(40)]

def update(n, l, r, i, val):
    # print(n, l, r, i)
    # put at index i value val
    if l == r == i:
        # leaf is value of node
        a[n] = val
    else:
        m = (l + r) // 2
        if i <= m:
            # left branch: 2*n
            update(2*n, l, m, i, val)
        else:
            # right branch: 2*n+1
            update(2*n+1, m+1, r, i, val)
        # update with sum left and right branches
        a[n] = a[2*n] + a[2*n+1]

def query(n, l, r, li, ri):
    if l == r == li == ri:
        return a[n]
    else:
        m = (l + r) // 2
        if ri <= m:
            return query(2*n, l, m, li, ri)
        elif li > m:
            return query(2*n+1, m+1, r, li, ri)
        else:
            return query(2*n, l, m, li, m) + query(2*n+1, m+1, r, m+1, ri)

n = 10
for i in range(1, n+1):
    update(1, 1, n, i, i)
    print(a)

print(a)
for x, y in [(1,3), (4,7), (1,5), (3,10), (2,8)]:
    r = query(1, 1, n, x, y)
    print(f'sum [{x},{y}] =', r, r == sum(range(x, y+1)))

