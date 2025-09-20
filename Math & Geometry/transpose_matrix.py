'''
Transpose Matrix
You are given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 100,000
-1,000,000,000 <= matrix[i][j] <= 1,000,000,000
'''

def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """
    Implement transpose
    """

# Test Cases
matrix = [[2,1], [-1,3]]

assert transpose(matrix) == [[2,-1], [1,3]]

matrix = [[1,0,5], [2,4,3]]

assert transpose(matrix) == [[1,2], [0,4], [5,3]]