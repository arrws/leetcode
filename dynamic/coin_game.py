# 2 player game: each player selects either the first or last coin from the row, and receives the value of that coin.
# a[i][j] max value you can colect from coins i to j
# select v[i] and then get min(v[i+1], v[j])
# select v[j] and then get min(v[i], v[j-1])


def coin_game(v):
    a = [[0 for _ in range(len(v))] for _ in range(len(v))]

    # for games of 1, 2, ... n coins
    for k in range(len(v)):
        i = 0
        j = k
        while j < len(v):
            # ... i, i+1, i+2 ... j-2, j-1, j ...
            x = a[i+2][j]   if i+2 < j   else 0 # player selects v[i] and opponent v[i+1]
            y = a[i+1][j-1] if i+1 < j-1 else 0 # player selects v[i] and opponent v[j]
            z = a[i][j-2]   if   i < j-2 else 0 # player selects v[j] and opponent v[j-1]
            a[i][j] = max(v[i]+min(x,y), v[j]+min(y,z)) # opponent will minimize player's gain
            i += 1
            j += 1

    # for k in a: print(k)
    print(a[0][-1])

coin_game([8, 15, 3, 7])
