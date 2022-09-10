# undirected graph
# complexity V*(V+E)
INF = 999

def dfs(G, x, p, u):
    for y in range(len(G[0])):
        # if x math y and y available
        if G[x][y] and u[y] == 0:
            u[y] = 1 # visited y

            # try to make it work
            # if y not matched with other x
            # OR previous x of y has an alternative
            if p[y] == -1 or dfs(G, p[y], p, u):
                p[y] = x
                return True
    return False

def max_matching(G):
    # len(G) ~ people
    # len(G[0]) ~ jobs

    # what x corresponds to each y
    p = [-1 for _ in range(len(G[0]))]

    r = 0
    for x in range(len(G)):
        # next x hasn't seen any y
        u = [0 for _ in range(len(G[0]))]

        # can x get an y?
        if dfs(G, x, p, u):
            r += 1

    print(r)

graph = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1]
]
max_matching(graph)
