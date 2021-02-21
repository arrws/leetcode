def word_break(s, words):
    # can i split sentence into words?
    max_len = len(max(words, key=len))

    a = [0 for _ in range(len(s)+1)]
    a[0] = 1

    for i in range(len(s)):
        if a[i] == True:
            limit = min(i + max_len, len(s))
            for j in range(i, limit):
                if s[i:j+1] in words:
                    a[j+1] = 1

    print(True if a[-1] == 1 else False) # True False


def word_comb(s, words):
    # show all possible breakings
    result = []

    def dfs(dp, k, path):
        if k == 0:
            result.append(path)
            return
        for word in dp[k]:
            if path:
                dfs(dp, k - len(word), word + " " + path)
            else:
                dfs(dp, k - len(word), word)

    wset = set(words)
    max_len = len(max(words, key=len))

    # inverse logic starting with end of word
    a = [[] for _ in range(len(s) + 1)]
    a[0] = True

    for i in range(1, len(s) + 1):
        for j in range(max(0, i - max_len), i):
            if a[j] and s[j:i] in wset:
                a[i].append(s[j:i])

    dfs(a, len(s), "")
    print(result)


word_break("leetcodesucks", ["leet", "code", "sucks"])
word_comb("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])

