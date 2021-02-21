
def long_dup_str(s):
    ss = s+s
    mx = 0
    imx = 0
    for i in range(len(s)): # i is translation
        k = 0
        for j in range(len(s)):
            if ss[i+j] == s[j]:
                k += 1
            else:
                if mx < k:
                    mx = k
                    imx = j - k
                k = 0
    return s[imx:imx+mx]

print(long_dup_str("banana"))

