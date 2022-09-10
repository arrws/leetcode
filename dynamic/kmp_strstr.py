def strstr(s, a):
    l = len(a)
    ass = sum([ord(x) for x in a])
    sass = sum([ord(x) for x in s[:l]])
    for i in range(len(s)-l+1):
        if sass == ass:
            ok = 1
            for j in range(len(a)):
                if s[i+j] != a[j]:
                    ok = 0
                    break
            if ok == 1:
                print(i)
        sass -= ord(s[i])
        if i+l < len(s):
            sass += ord(s[i+l])
    print("")

strstr("abcabbbasab", "ab")
strstr("xabcabcbxbasabc", "abc")


def kmp_search(s, x):
    # preprocess target string
    u = preprocess(x)
    k = 0
    i = 0
    while i<len(s):
        if s[i] == x[k]:
            k += 1
            i += 1
        if k == len(x):
            print(i-k)
            k = u[k-1]
        elif i<len(s) and x[k] != s[i]:
            if k != 0:
                k = u[k-1]
            else:
                i += 1

def preprocess(x):
    u = [0]*len(x)
    k = 0
    i = 1
    while i<len(x):
        if x[i] == x[k]:
            k += 1
            u[i] = k
            i += 1
        else:
            if k != 0:
                k = u[k-1]
            else:
                u[k] = 0
                i += 1
    # print(u)
    return u

kmp_search("ABABDABACDABABCABAB", "ABAB")


# Version II

def kmp_search_2(s, x):
    s = "_"+s
    x = "_"+x

    # preprocess target string
    u = preprocess_2(x)

    k = 0
    for i in range(1,len(s)):
        while k > 0 and s[i] != x[k+1]:
            k = u[k]
        if x[k+1] == s[i]:
            k += 1
        if k == len(x)-1:
            print(i-k)
            k = u[k]

def preprocess_2(x):
    u = [0]*len(x)
    k = 0
    for i in range(2,len(x)):
        while k > 0 and x[i] != x[k+1]:
            k = u[k]
        if x[k+1] == x[i]:
            k += 1
        u[i] = k
    # print(u)
    return u

kmp_search_2("ABABDABACDABABCABAB", "ABAB")
