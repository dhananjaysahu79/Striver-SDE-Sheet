# The question seems to be easy as we can easily solve it using (m+n)
# extra space.
# But the level tagged in leetcode is Medium,
# The reason is you have to solve it in O(1) space.

# Approach O(m*n) time and O(1) space:
# We will use the first row and first column to store which which column
# or row will going to be zeroed. and we would take one variable 'row' to
# mark if we get 0 in 0th row at any index.
def solveMatrix(matrix,m,n):
    row = 1
    for i in range(m):
        for j in range(n):
            if i == 0:
                if matrix[i][j] == 0: row = 0
            elif matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if i == 0:
                if row == 0: matrix[i][j] = 0
            elif matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0
    return matrix

m,n = map(int,input().split())
matrix = []
for _ in range(m):
    matrix.append(list(map(int,input().split())))
print(*solveMatrix(matrix,m,n), sep = '\n')
