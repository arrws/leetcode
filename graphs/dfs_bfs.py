# dir/undir graph
# complexity V+E

def dfs(start, stop, v, u, path):
    if start == stop:
        print(path)
        return
    for f in v[start]:
        if u[f] == 0:
            u[f] = 1
            path.append(f)
            dfs(f, stop, v, u, path)
            path.pop(-1)

a = [[1,3], [0,2], [1], [0,2,6], [5], [4,6,1], [3]]
u = [0 for _ in range(len(a))]
dfs(4, 0, a, u, [])



# undir graph
# complexity V+E

def dfs(start, v, u, k):
    for f in v[start]:
        if u[f] == 0:
            u[f] = k
            dfs(f, v, u, k)

def connected_comp(v):
    k = 0
    u = [0 for _ in range(len(v))]
    for i in range(len(v)):
        if u[i] == 0:
            k += 1
            dfs(i, v, u, k)
    print(k)
    print(u)

connected_comp([[1,3], [0,2], [1,3], [0,2], [5], [4]])



# dir/undir graph
# complexity V+E

def bfs(start, v):
    u = [0 for _ in range(len(v))]
    u[start] = 1
    q = [start]
    while len(q) > 0:
        x = q.pop(0)
        for f in v[x]:
            if u[f] == 0:
                q.append(f)
                u[f] = u[x] + 1
    print(u)

a = [[1,3], [0,2], [1], [0,2,6], [5], [4,6,1], [3]]
bfs(0, a)
