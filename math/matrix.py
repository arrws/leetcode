
# 0 1 2 3
# 1 2 3 4
# 2 3 4 5
# 6 7 8 9

def search_ordered_matrix(matrix, target):
    # row/column sorted asc left-right/top-bottom
    if matrix == []:
        return False
    i = 0
    j = len(matrix[0])-1
    while i < len(matrix) and j >= 0:
        if matrix[i][j] == target:
            return True
        if matrix[i][j] < target:
            i += 1
        else:
            j -= 1
    return False


def spiralOrder(matrix):
    # traverse matrix in spiral order
    if matrix == []: return []
    N = len(matrix)
    M = len(matrix[0])
    r = []
    k = 0

    while len(r) < M*N:
        n = N - k
        m = M - k

        for x in range(k, m):
            r.append(matrix[k][x])
        for x in range(k+1, n):
            r.append(matrix[x][m-1])

        if len(r) >= M*N: break

        for x in range(m-2, k-1, -1):
            r.append(matrix[n-1][x])
        for x in range(n-2, k, -1):
            r.append(matrix[x][k])

        k += 1
    return r


def rotateNinety(matrix):
    # rotate 90 degrees
    N = len(matrix[0])
    for i in range(N):
        for j in range(i, N-i-1):
            # matrix[i][j]            = matrix[N-j-1][i]
            # matrix[j][N-i-1]        = matrix[i][j]
            # matrix[N-i-1][N-j-1]    = matrix[j][N-i-1]
            # matrix[N-j-1][i]        = matrix[N-i-1][N-j-1]
            matrix[i][j], matrix[j][N-i-1], matrix[N-i-1][N-j-1], matrix[N-j-1][i] = matrix[N-j-1][i], matrix[i][j], matrix[j][N-i-1], matrix[N-i-1][N-j-1]

