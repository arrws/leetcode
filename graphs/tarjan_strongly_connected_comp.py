# directed graph
# complexity V+E
# based on articulation points

t = 0

def traverse(G, x, low, disc, u, r):
    global t
    disc[x] = t
    low[x] = t
    u[x] = 1
    t += 1
    r.append(x)

    for v in G[x]:
        # not visited yet
        if disc[v] == -1:
            # add in the stack
            traverse(G, v, low, disc, u, r)
            # once done update earliest link
            low[x] = min(low[x], low[v])
        # visited and in stack
        elif u[v] == 1:
            # update earliest link
            low[x] = min(low[x], disc[v])

    k = -1
    # if the earlier link of x is itself then
    # x is the root of a SCP
    if low[x] == disc[x]:
        while k != x:
            k = r.pop() # remove from stack
            u[x] = 0 # not on current stack anymore
            print(k, end=" ")
        print("")

def tarjan(G):
    n = len(G)
    disc = [-1 for _ in range(n)] # link time
    low = [-1 for _ in range(n)] # earliest link time
    r = [] # stack
    u = [0 for _ in range(n)] # is node in in stack ?

    for i in range(n): # in case of disconnected graph
        if disc[i] == -1:
            traverse(G, i, low, disc, u, r)

G = [[2,3], [0], [1], [4], []]
tarjan(G)



# ???
# bridges strong comp ??? oriented graph

def solve(graph):
    low = [float("inf") for x in range(len(graph))]
    t = [-1 for x in range(len(graph))]
    k = 0

    apoints = set()
    bridges = set()

    # for biconnected components
    s = []

    def dfs(x, p):
        nonlocal k
        k += 1
        t[x] = k
        low[x] = k

        for y in graph[x]:
            # tree edge
            if t[y] == -1:
                s.append((x, y))
                dfs(y, x)
                low[x] = min(low[x], low[y])

                # found articulation point
                if low[y] >= t[x]:
                    apoints.add(x)

                    # found biconnected component
                    # pop everything new put in stack
                    while s[-1] != (x, y):
                        e = s.pop(-1)[1]
                        print(e, end=" ")
                    e = s.pop(-1)[1]
                    print(e)

                # found bridge
                if low[y] > t[x]:
                    bridges.add((x, y))

            # backedge
            elif y != p and t[y] < t[x]:
                s.append((x, y))
                low[x] = min(low[x], t[y])

    dfs(0, -1)

    print(apoints)
    print(bridges)

G = [[2,3], [0], [1], [4], []]
solve(G)


# undirected graph
# complexity V+E

INF = 999
t = 0

def traverse(G, x, u, p, low, disc):
    global t
    children = 0
    disc[x] = t
    low[x] = t
    u[x] = 1
    t += 1

    for v in G[x]:
        # not visited yet
        if u[v] == 0:
            p[v] = x
            children += 1

            traverse(G, v, u, p, low, disc)
            # once done update earliest link
            low[x] = min(low[x], low[v])

            # is articulation point if:
            # x root and has >2 children
            if p[x] == -1 and children > 1:
                print(x)
            # x's child has lower low than x
            if p[x] != -1 and low[v] >= disc[x]:
                print(x)
        # already visited
        elif v != p[x]:
            low[x] = min(low[x], disc[v])


def articulation_points(G):
    # ~ bipartite components
    n = len(G)
    u = [0 for _ in range(n)] # visited
    p = [-1 for _ in range(n)] # parent

    disc = [INF for _ in range(n)] # discovery/link time
    low = [INF for _ in range(n)] # earliest dicovery/link time
    # low[x] = min(disc[x], disc[ancestor x])

    for i in range(n):
        if u[i] == 0:
            traverse(G, i, u, p, low, disc) # dfs


# edges = [[1,0], [0,2], [2,1], [0,3], [3,4]]
G = [[2, 3, 1], [0, 2], [1, 0], [4, 0], [3]]
articulation_points(G)
