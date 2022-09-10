# undirected weighted graph
# complexity V^2
INF  = 999

def prim_min_span_tree(g):
    V = len(g)
    used = set()
    parent = [-1 for _ in range(V)]
    parent[0] = 0
    d = [INF for _ in range(V)]
    d[0] = 0

    for _ in range(V):
        # x = get min dist vertex
        dist = INF
        for v in range(V):
            if v not in used and d[v] < dist:
                dist = d[v]
                x = v

        used.add(x)
        for y in range(len(g[x])):
            if g[x][y]>0: # if x y connected
                if y not in used and d[y] > g[x][y]:
                    # if can improve distance
                    d[y] = g[x][y]
                    parent[y] = x

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
