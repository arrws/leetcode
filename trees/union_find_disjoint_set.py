# get root
def find(p, x):
    r = x
    while p[r] != r:
        r = p[r]

    # compress
    while p[x] != x:
        x = p[x]
        p[x] = r

    return r

def union(p, x, y):
    x = find(p, x)
    y = find(p, y)

    # if x>y:
    #     x,y = y,x

    p[y] = x

# example application
def find_cycle(G):
    p = [i for i in range(len(G))]

    for x in range(len(G)):
        for y in G[x]:
            if find(p, x) == find(p, y):
                print("True")
                return
            union(p, x, y)
    print("False")

G = [[1], [2], [0]]
find_cycle(G)
