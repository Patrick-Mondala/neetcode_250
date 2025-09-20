'''
Min Cost Climbing Stairs
You are given an array of integers cost where cost[i] is the cost of taking a step from the ith floor of a staircase. After paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.

You may choose to start at the index 0 or the index 1 floor.

Return the minimum cost to reach the top of the staircase, i.e. just past the last index in cost.

Constraints:

2 <= cost.length <= 100
0 <= cost[i] <= 100
'''

def minCostClimbingStairs(cost: list[int]) -> int:
    """
    Implement minCostClimbingStairs
    """

# Test Cases
cost = [1,2,3]
assert minCostClimbingStairs(cost) == 2

cost = [1,2,1,2,1,1,1]
assert minCostClimbingStairs(cost) == 4