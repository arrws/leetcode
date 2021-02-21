# directed graph
# complexity V+E
# based on topological sort

def get_order(G, x, u, r):
    # for topological order
    u[x] = 1
    for v in G[x]:
        if u[v] == 0:
            get_order(G, v, u, r)
    r.append(x)

def dfs(G, x, u):
    u[x] = 1
    print(x, end=' ')
    for v in G[x]:
        if u[v] == 0:
            dfs(G, v, u)

def kosaraju(G):
    # get topological order
    u = [0 for _ in range(len(G))]
    r = []
    for x in range(len(G)):
        if u[x] == 0:
            get_order(G, x, u, r)

    # inverse graph
    G_inv = [ [] for _ in range(len(G)) ]
    for i, friends in enumerate(G):
        for f in friends:
            G_inv[f].append(i)
    # print(G_inv)
    print(r)

    # kosaraju
    u = [0 for _ in range(len(G))]
    while len(r) > 0:
        x = r.pop(-1)
        if u[x] == 0:
            dfs(G_inv, x, u)
            print("")

G = [[2,3], [0], [1], [4], []]
kosaraju(G)

