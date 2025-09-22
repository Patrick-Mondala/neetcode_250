'''
Island Perimeter
You are given a row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1.

Return the perimeter of the island.

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid.
'''

# Time Complexity: O(N * M) where N is the size of a row in the grid, and M is the size of a column in the grid, due to iterating over every cell in the grid
# Space Complexity: O(1) due to using constant extra space
def islandPerimeter(grid: list[list[int]]) -> int:
    ROW_SIZE = len(grid)
    COL_SIZE = len(grid[0])
    DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    result = 0

    def getPerimeter(row, col):
        perimeter = 0

        for r, c in DIR:
            if row + r < 0 or row + r == ROW_SIZE:
                perimeter += 1
            elif col + c < 0 or col + c == COL_SIZE:
                perimeter += 1
            elif grid[row + r][col + c] == 0:
                perimeter += 1
        
        return perimeter
    
    for row in range(ROW_SIZE):
        for col in range(COL_SIZE):
            if grid[row][col]:
                result += getPerimeter(row, col)

    return result

# Test Cases
grid = [
    [1,1,0,0],
    [1,0,0,0],
    [1,1,1,0],
    [0,0,1,1]
]
assert islandPerimeter(grid) == 18

grid = [[1,0]]
assert islandPerimeter(grid) == 4