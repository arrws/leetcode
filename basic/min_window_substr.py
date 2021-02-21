import collections

def min_window(s, t):
    # min substring from s wich contains all characters from t
    r = s + "fuck"
    du = collections.defaultdict(int)
    d = {}
    for x in t:
        du[x] += 1
        d[x] = 0

    fs = []
    for i in range(len(s)):
        if du.get(s[i], -1) != -1:
            fs.append([s[i], i])

    req = len(du)
    k = 0
    i, j = 0, 0
    while j<len(fs):
        # expand window to right
        d[fs[j][0]] += 1
        if d[fs[j][0]] == du[fs[j][0]]:
            k += 1

        # maybe shrink window from left
        while k == req:
            # check the new window
            w = s[fs[i][1]:fs[j][1]+1]
            if len(r) > len(w):
                r = w

            d[fs[i][0]] -= 1
            if d[fs[i][0]] < du[fs[i][0]]:
                k -= 1
            i += 1
        j += 1

    if len(r) < len(t) or len(r) > len(s):
        return ""
    return r

print(min_window("adobecodebanc", "abc"))

