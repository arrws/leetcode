
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





#### C++

##include <iostream>
#using namespace std;

#void compute (int **matrix, int r, int m, int n) {
#    int k = (n<m)? n : m;
#    int *flatten;
#    flatten  =  malloc((m*2+(n-2)*2)*sizeof(int));

#    for (int i = 0; i<k; i++) {
#        if ((i+1)*2 > k)
#			break;

#		int p = 0;
#        // top row, left to right
#        for (int j = i; j<n-i; j++) {
#            flatten[p++]  =  matrix[i][j];
#        }
#        // right column, top to bottom
#        for (int j = i+1; j<m-i; j++) {
#            flatten[p++]  =  matrix[j][n-1-i];
#        }
#        // bottom row, right to left
#        for (int j = n-2-i; j>= i; j--) {
#            flatten[p++]  =  matrix[m-1-i][j];
#        }
#        // left column, bottom to top
#        for (int j = m-2-i; j>i; j--) {
#            flatten[p++]  =  matrix[j][i];
#        }

#        int start = r%p; // rotate r times
#        if (start == 0)
#			continue;

#		// top row, left to right
#		for (int j = i; j<n-i; j++) {
#			matrix[i][j]  =  flatten[start];
#			start  =  (start+1) % p;
#		}
#		// right column, top to bottom
#		for (int j = i+1; j<m-i; j++) {
#			matrix[j][n-1-i]  =  flatten[start];
#			start  =  (start+1) % p;
#		}
#		// bottom row, right to left
#		for (int j = n-2-i; j>= i; j--) {
#			matrix[m-1-i][j]  =  flatten[start];
#			start  =  (start+1) % p;
#		}
#		// left column, bottom to top
#		for (int j = m-2-i; j>i; j--) {
#			matrix[j][i]  =  flatten[start];
#			start  =  (start+1) % p;
#		}
#    }
#    if (!flatten)
#		free(flatten);
#}

#int main()
#{
#	int a[100][100];
#	int m, n, r;

#    cin >> m >> n >> r;
#    for(int i  =  0;i < m;i++){
#        for(int j  =  0;j < n;j++){
#            cin >> a[i][j];
#        }
#    }

# compute(&a, r, m, n);

#    for(int i  =  0;i < m;i++){
#        for(int j  =  0;j < n;j++){
#            cout << a[i][j] << ' ';
#        }
#        cout << '\n';
#    }
#    return 0;
#}

