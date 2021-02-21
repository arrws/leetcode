# directed weighted graph
# V^3
INF  = 999

def floyd_warshall(d):
    V = len(d)
    for k in range(V): # order matters
        for i in range(V):
            for j in range(V):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    for i in d:
        print(i)


d = [[0,5,INF,10],
     [INF,0,3,INF],
     [INF, INF, 0,   1],
     [INF, INF, INF, 0]
    ]
floyd_warshall(d)
