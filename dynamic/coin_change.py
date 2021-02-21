# fewest number of coins that you need to make a given amount

def coin_change(coins, k):
    r = [0] + [k+1] * k

    for i in range(1, k+1):
        for c in coins:
            if i >= c:
                r[i] = min(r[i], r[i-c] + 1)

    if r[k] == k+1:
        return -1
    return r[k]

print(coin_change([1, 2, 5], 11))
