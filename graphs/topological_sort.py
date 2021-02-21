# directed graph
# complexity V+E

def topological_sort(G):
    u = [0 for _ in range(len(G))]
    r = []

    def search(x):
        u[x] = 1
        for y in G[x]:
            if u[y] == 1:
                print("ERR cycle")
                break
            if u[y] == 0:
                search(y)
        u[x] = 2
        r.append(x)

    for x in range(len(G)):
        if u[x] == 0:
            search(x)
    r.reverse()
    print(r)


def topological_sort_kahn(G):
    # Kahn algorithm
    # compute in-degrees of vertices
    in_degree = [0 for _ in range(len(G)+1)]
    for edge in G:
        for x in edge:
            in_degree[x] += 1

    print(in_degree)
    queue = []
    for i in range(len(G)): # enqueue all vertices with indegree 0
        if in_degree[i] == 0:
            queue.append(i)

    k = 0 # count vizited vertices
    top_order = [] # topological order

    while queue:
        u = queue.pop(0)
        top_order.append(u)

        for i in G[u]:
            in_degree[i] -= 1 # update in-degree
            # if in-degree becomes zero add it to queue
            if in_degree[i] == 0:
                queue.append(i)
        k += 1

    if k != len(G): # check if there was a cycle
        print("ERR cycle")
    return reversed(top_order) # run order to meet dependencies


G = [[], [], [3], [1], [0,1], [2,0]]

topological_sort(G)
topological_sort_kahn(G)

