# directed weighted graph
# (V+E)logV

import heapq
INF  = 999

def dijkstra(start, stop, G):
    p = [i for i in range(len(G))] # parent
    d = [INF for _ in range(len(G))] # shortest dist
    d[start] = 0
    q = [(0, start)]

    while len(q) > 0:
        _, x = heapq.heappop(q)

        for y in range(len(G)):
            if G[x][y] != 0 and d[y] > d[x] + G[x][y]:
                d[y] = d[x] + G[x][y] # update shortest dist to y
                p[y] = x # update parent
                # will enter multiple times but not processed
                heapq.heappush(q, (d[y], y))

    print(p)
    print(d)
    print(d[stop])


def uniform(start, stop, G):
    # for infinite graphs
    p = [i for i in range(len(G))] # parent
    used = set()
    q = [(0, start)]

    while len(q) > 0:
        dx, x = heapq.heappop(q)

        if x not in used:
            used.add(x)

            if x == stop:
                return dx # min distance to x

            for y in range(len(G)):
                if G[x][y] != 0: # x and y are connected
                    if y not in used:
                        p[y] = x
                        heapq.heappush(q, (dx + G[x][y], y))

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

dijkstra(0, 7, G)
uniform(0, 7, G)

