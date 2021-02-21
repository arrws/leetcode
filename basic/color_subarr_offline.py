def paint_subarr(queries, n):
    # keep in a the closer right uncolored cell
    a = [i for i in range(n)]
    colors = [-1 for i in range(n)]

    def get_root(x):
        if a[x] == x:
            return x
        a[x] = get_root(a[x])
        return a[x]

    for query in queries[::-1]:
        x, y, c = query
        while x <= y and x<n:
            x = get_root(x)
            colors[x] = c
            a[x] = x + 1
    print(colors)

paint_subarr([[5, 7, 1],
              [2, 4, 5],
              [3, 6, 2],
              [8, 9, 3],
              [5, 6, 4]],
             15)




