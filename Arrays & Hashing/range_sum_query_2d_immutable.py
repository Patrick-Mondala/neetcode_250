'''
Range Sum Query 2D Immutable
You are given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-10,000 <= matrix[i][j] <= 10,000
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
At most 10,000 calls will be made to sumRegion.
'''

class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        """
        Implement NumMatrix init
        """

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Implement sumRegion
        """


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# Test Cases
nm = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
assert nm.sumRegion(2, 1, 4, 3) == 8
assert nm.sumRegion(1, 1, 2, 2) == 11
assert nm.sumRegion(1, 2, 2, 4) == 12