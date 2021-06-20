# directed weighted graph
# V^2 * E
INF = 999


def bfs(G, level, source, sink, p):
    q = [source]
    level[source] = 0
    k = 1
    while len(q) > 0:
        new_q = []
        while len(q) > 0:
            x = q.pop(0)
            for v, cap in enumerate(G[x]):
                if level[v] == -1 and cap > 0:
                    new_q.append(v)
                    level[v] = k
                    p[v] = x
        q = new_q
        k += 1
    if level[sink] > -1:
        return True
    return False


def dfs(G, level, x, sink, p):
    if x == sink:
        return INF
    for v, cap in enumerate(G[x]):
        if level[v] == level[x] + 1:
            p[v] = x
            aug_flow = dfs(G, level, v, sink, p)
            if aug_flow > 0:
                return min(cap, aug_flow)
    return 0


def max_flow(G):
    source = 0
    sink = len(G) - 1
    p = [-1 for _ in range(len(G))]
    level = [-1 for _ in range(len(G))]
    max_flow = 0

    while bfs(G, level, source, sink, p):
        # find min residual edge filled by dfs
        print(level)
        aug_flow = dfs(G, level, source, sink, p)
        print(aug_flow, max_flow)

        # update
        while aug_flow > 0:
            max_flow += aug_flow

            # update residual graph
            x = sink
            while(x != source):
                G[p[x]][x] -= aug_flow
                G[x][p[x]] += aug_flow  # residual graph for undos
                x = p[x]

            aug_flow = dfs(G, level, source, sink, p)

        level = [-1 for _ in range(len(G))]

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

