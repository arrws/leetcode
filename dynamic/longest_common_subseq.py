def longest_common_subseq(a, b):
    a = "_"+a
    b = "_"+b
    q = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]
    # q[i][j] max substring matching for a[:i+1], b[:j+1]

    for i in range(1,len(a)):
        for j in range(1,len(b)):
            # if letter match plus 1 from prev letters matching
            if a[i] == b[j]:
                q[i][j] = q[i-1][j-1] +1
            else:
            # else max matching ignoring current letter from a or b
                q[i][j] = max(q[i-1][j], q[i][j-1])
    # for i in q: print(i)

    s = ""
    i, j = len(a)-1, len(b)-1
    while i>0 and j>0:
        if a[i] == b[j]:
            s = a[i]+s
            i -= 1
            j -= 1
        elif q[i][j-1] > q[i-1][j]:
            j -= 1
        else:
            i -= 1
    print(s)

longest_common_subseq("AGGTAB", "GXTXAYB")
