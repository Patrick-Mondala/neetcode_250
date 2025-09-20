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

def islandPerimeter(grid: list[list[int]]) -> int:
    """
    Implement islandPerimeter
    """

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