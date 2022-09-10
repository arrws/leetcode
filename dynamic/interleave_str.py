def interleave_str(s1, s2, s3):
    # can s3 be formed by interleaving s1 and s2 ?
    n, m = len(s1), len(s2)
    if len(s3) != n + m:
        return False

    dp = [False for _ in range(m + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == j ==0:
                dp[j] = True
            elif i == 0:
                dp[j] = dp[j-1] and s2[j-1] == s3[i+j-1]
            elif j == 0:
                dp[j] = dp[j] and s1[i-1] == s3[i+j-1]
            else:
                dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])

    return dp[-1]

print(interleave_str("aabcc", "dbbca", "aadbbcbcac"))
