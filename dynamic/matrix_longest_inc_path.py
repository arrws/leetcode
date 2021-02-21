# longest increasing path from (0, 0) to (n, m)

def find_path_dp(mat):
    MAX = 9999
    dp = [[-1 for i in range(MAX)] for i in range(MAX)]

    def fun(n, m, x, y):
        # If value not calculated yet.
        if (dp[x][y] < 0):
            result = 0

            # If reach bottom left cell, return 1.
            if (x == n - 1 and y == m - 1):
                dp[x][y] = 1
                return dp[x][y]

            # If reach the corner of the matrix.
            if (x == n - 1 or y == m - 1):
                result = 1

            # If value greater than below cell.
            if (x + 1 < n and mat[x][y] < mat[x + 1][y]):
                result = 1 + fun(n, m, x + 1, y)

            # If value greater than left cell.
            if (y + 1 < m and mat[x][y] < mat[x][y + 1]):
                result = max(result, 1 + fun(n, m, x, y + 1))

            dp[x][y] = result

        return dp[x][y]

    return fun(len(mat), len(mat[0]), 0, 0)

mat = [[1, 2, 3, 4 ],
        [2, 2, 3, 4 ],
        [3, 2, 3, 4 ],
        [4, 5, 6, 7 ]]

print(find_path_dp(mat))

