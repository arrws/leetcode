def count_pal(s):
    # dynamic prog: count the number of palindromes in a string
    s = "." + s
    a = [[False for _ in range(len(s)+1)] for _ in range(len(s)+1)]
    k = 0
    for d in range(len(s)): # count palindromes of length 1, 2, ... n
        # to verify palindrome from i to j
        for i in range(1, len(s)-d):
            j = i + d
            # check if elements at i and j are equal
            if s[i] == s[j]:
                # and check if string from i+1 and j-1 was palindrome
                if i+1 >= j-1:
                    a[i][j] = True
                else:
                    a[i][j] = a[i+1][j-1]
                if a[i][j]:
                    k += 1
    return k

def manacher_pal(s):
    # Manacher's algorithm
    s = "@#" + "#".join(s) + "#$"
    # print(s)
    k = 0
    for i in range(1, len(s)-1):
        r = 0
        while s[i + r] == s[i - r]:
            r += 1
        # print(r, s[i-r:i+r])
        k += r // 2
    return k

print(count_pal("acdababba"))
print(manacher_pal("acdababba"))
