def root(p, x):
    r = x
    while p[r] != r:
        r = p[r]
    while p[x] != x:
        x, p[x] = p[x], r
    return x

def kruskal_min_span_tree(g):
    V = len(g)
    g = sorted(g, key=lambda x: x[2])
    a = [i for i in range(V)] # roots set
    tree = []

    # loop edges
    for [x, y, d] in g:
        xr = root(a, x)
        yr = root(a, y)
        if xr != yr:
            a[xr] = yr
            tree.append([x, y, d])

    for i in tree:
        print(i)

# [vertex, vertex, dist]
g = [
    [0, 1, 10],
    [0, 2, 6],
    [0, 3, 5],
    [1, 3, 15],
    [2, 3, 4]
    ]
kruskal_min_span_tree(g)
