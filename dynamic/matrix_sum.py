def buildMatrix(matrix):
    if not matrix: return
    m = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
    for i in range(1, len(matrix)+1):
        for j in range(1, len(matrix[0])+1):
            m[i][j] = m[i-1][j] + m[i][j-1] - m[i-1][j-1] + matrix[i-1][ j-1]
    return m

def sumRegion(m, i1, j1, i2, j2):
    return m[i2+1][j2+1] - m[i1][j2+1] - m[i2+1][j1] + m[i1][j1]

matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
m = buildMatrix(matrix)
print(sumRegion(m, 2, 1, 4, 3))
