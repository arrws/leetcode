# undirected weighted graph
# complexity V^2
INF  = 999

def prim_min_span_tree(g):
    V = len(g)
    u = [0 for _ in range(V)]
    parent = [-1 for _ in range(V)]
    parent[0] = 0
    d = [INF for _ in range(V)]
    d[0] = 0

    for _ in range(V):
        # x = get min dist vertex
        dist = INF
        for v in range(V):
            if u[v] == 0 and d[v] < dist:
                dist = d[v]
                x = v

        u[x] = 1
        for f in range(len(g[x])):
            if u[y] == 0 and d[f] > g[x][f] and g[x][f]>0:
                d[f] = g[x][f]
                parent[f] = x

    for i, x in enumerate(parent):
        print([i,x], d[i])

g = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
    ]
prim_min_span_tree(g)
