# given multiple objects of weight w and profit p
# maximum profit by stealing objects weiting max_weight in total

def knapsack(max_weight, w, p):
    a = [[ 0 for _ in range(max_weight+1)] for _ in range(len(p)+1)]

    # go throught all objects
    for i in range(1, len(p)+1):
        # if you take 1, 2,  ... max_weight load
        for j in range(1, max_weight+1):
            a[i][j] = a[i-1][j]
            if w[i-1] <= j:
                a[i][j] = max(a[i][j], p[i-1] + a[i-1][j-w[i-1]])
        # for x in a: print(x)

    s = []
    i, j = len(p), max_weight
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
