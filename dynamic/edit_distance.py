# find the minimum number of edits (insert, remove, replace) required to convert str1 into str2
def edit_distance(s1, s2):
    m = len(s1)+1
    n = len(s2)+1
    v = [[0] * n for _ in range(m)]

    # first sring is empty all insert
    for i in range(m):
        v[i][0] = i

    # second sring is empty all remove
    for j in range(n):
        v[0][j] = j

    for i in range(1, m):
        for j in range(1, n):
            # last characters the same do nothing
            if s1[i - 1] == s2[j - 1]:
                v[i][j] = v[i - 1][j - 1]
            else:
                # take min of remove, insert or replace
                v[i][j] = 1 + min(v[i - 1][j], v[i][j - 1], v[i - 1][j - 1])

    print(v[-1][-1])

edit_distance("sunday", "saturday")
