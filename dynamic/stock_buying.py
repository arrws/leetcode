def max_profit(k: int, prices: list[int]):
    # Say you have an array for which the ith element is the price of a given stock on day i.
    # Design an algorithm to find the maximum profit.
    # You may complete at most k transactions.
    # You may not engage in multiple transactions at the same time.

    if len(prices) < 1:
        return 0

    if len(prices)//2 < k:
        s = 0
        u = prices[0]
        for p in prices:
            s += max(0, p-u)
            u = p
        return s

    # print(prices)

    # max profit until time i
    dp = [0 for _ in range(len(prices))]
    for _ in range(k): # can do k transactions
        mn = prices[0]
        mx = 0
        # compute for each transaction
        for i in range(1, len(prices)):
            # keep track of min buypoint
            mn = min(mn, prices[i] - dp[i])
            mx = max(mx, prices[i] - mn)
            dp[i] = mx
            # print(prices[i], mn, mx)
        # print(dp)
    return dp[-1]

print(max_profit(3, [1,4,16,6,10,8,2,10,4,20,1,3,2]))
