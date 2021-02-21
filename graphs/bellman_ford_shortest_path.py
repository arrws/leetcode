INF = 999

def bellman_ford(edges, n):
    d = [float('inf') for _ in range(n)]
    p = [-1 for _ in range(n)]
    d[0] = 0
    p[0] = 0

    k = 0
    while True:
        changed = False
        for (x, y, c) in edges:
            if d[y] < d[x] + c:
                d[y] = d[x] + c
                p[y] = x
                changed = True
        k += 1

        if k > n:
            print("Negative Cycle")
            break;

        if not changed:
            break

    print(d)
    print(p)


def bellman_ford(start, stop, G):
    d = [INF for _ in range(len(G))]
    p = [i for i in range(len(G))] # parent
    d[start] = 0
    ok = 0
    changed = 0

    while ok == 0 and changed == 0:
        changed = 1
        q = [start]
        while len(q) != 0:
            x = q.pop(0)
            for y in range(len(G)):
                if G[x][y] != 0 and d[y] > d[x] + G[x][y]:
                    d[y] = d[x] + G[x][y]
                    p[y] = x
                    q.append(y)
                    changed = 0
                    if y == stop:
                        ok = 1
                        break
    # print(d)
    print(p)
    print(d[stop])

G = [
[0, 4, 0, 0, 0, 0, 0, 8, 0],
[4, 0, 8, 0, 0, 0, 0, 11, 0],
[0, 8, 0, 7, 0, 4, 0, 0, 2],
[0, 0, 7, 0, 9, 14, 0, 0, 0],
[0, 0, 0, 9, 0, 10, 0, 0, 0],
[0, 0, 4, 14, 10, 0, 2, 0, 0],
[0, 0, 0, 0, 0, 2, 0, 1, 6],
[8, 11, 0, 0, 0, 0, 1, 0, 7],
[0, 0, 2, 0, 0, 0, 6, 7, 0]
]
edges = []
for i in range(len(G)):
    for j in range(len(G)):
        if G[i][j]:
            edges.append([i, j, G[i][j]])

# bellman_ford(0, 7, 9, edges)
bellman_ford(0, 7, G)
