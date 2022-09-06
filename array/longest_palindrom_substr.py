def longest_pal(s):
    if s == None: return ""
    if len(s) < 1: return ""

    def expand(i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return j-i-1

    x = 0
    y = 0
    for i in range(len(s)):
        l = max(expand(i, i), expand(i, i+1))
        if l > y-x:
            x = i - (l-1)//2
            y = i + l//2

    return s[x:y+1]

print(longest_pal("babad"))
