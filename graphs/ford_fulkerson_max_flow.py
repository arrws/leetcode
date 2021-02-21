# directed weighted graph
# (V+E)*E^2
INF = 999

def bfs(G, source, sink, p):
    u = [0 for _ in range(len(G))]
    q = [source]
    u[source] = 1
    while len(q) > 0:
        x = q.pop(0)
        for v, k in enumerate(G[x]):
            if u[v] == 0 and k > 0:
                q.append(v)
                u[v] = 1
                p[v] = x
    if u[sink] == 1:
        return True
    return False

def max_flow(G):
    # Edmonds Karp == Ford Fulkerson
    source = 0
    sink = len(G) -1
    p = [-1 for _ in range(len(G))]
    max_flow = 0
    while bfs(G, source, sink, p):
        # find min residual edge filled by bfs
        f = INF
        x = sink
        while(x != source):
            f = min(f, G[p[x]][x])
            x = p[x]
        # update
        max_flow += f
        x = sink
        while(x != source):
            G[p[x]][x] -= f
            G[x][p[x]] += f # residual graph for undos
            x = p[x]
    print(max_flow)

graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]
max_flow(graph)

