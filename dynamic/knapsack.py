# weight and profit

def knapsack(W, w, v): # W is max weight
    a = [[ 0 for _ in range(W+1)] for _ in range(len(v)+1)]

    for i in range(1, len(v)+1):
        for j in range(1, W+1): # if you take 1, 2,  ... W load
            a[i][j] = a[i-1][j]
            if w[i-1] <= j:
                a[i][j] = max(a[i][j], v[i-1] + a[i-1][j-w[i-1]])
        # for x in a: print(x)

    s = []
    i, j = len(v), W
    while i > 0:
        if w[i-1] <= j and a[i-1][j] < a[i][j]:
            s.append(i)
            j -= w[i-1]
        i -= 1

    print(a[-1][-1], s)

# [0, 0, 0, 0, 0]
# [0, 6, 6, 6, 6]
# [0, 6, 10, 16, 16]
# [0, 6, 10, 16, 18]
# [0, 8, 14, 18, 24]
# 24 [4, 2, 1]

knapsack(4, [1, 2, 3, 1], [6, 10, 12, 8])
