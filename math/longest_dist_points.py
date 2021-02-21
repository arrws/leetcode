import sys

# longest distance between 2 points

INF = float('inf')
n = int(sys.stdin.readline())
sx = [int(x) for x in sys.stdin.readline().split()]
sy = [0]
for x in sx:
    sy.append(x + sy[-1])
a = list(zip(range(len(sx)), sy[1:]))

def dist(x, y):
    return (x[0]-y[0])**2 + (x[1]-y[1])**2

def fun(a):
    if len(a) < 2 :
        return INF
    if len(a) == 2:
        return dist(a[0], a[1])
    m = len(a)//2
    s = min(fun(a[:m]), fun(a[m:]))
    mn = INF

    points = [x for x in a if abs(x[0]-a[m][0]) <= s]
    points = sorted(points, key=lambda x: x[1])

    for i in range(len(points)):
        j = i+1
        while j in range(i, min(i+8, len(points))):
            d = dist(points[j], points[i])
            mn = min(mn, d)
            j += 1

    return min(mn, s)

print(r)
r = fun(a)

