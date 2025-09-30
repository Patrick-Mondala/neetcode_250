'''
Min Cost Climbing Stairs
You are given an array of integers cost where cost[i] is the cost of taking a step from the ith floor of a staircase. After paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.

You may choose to start at the index 0 or the index 1 floor.

Return the minimum cost to reach the top of the staircase, i.e. just past the last index in cost.

Constraints:

2 <= cost.length <= 100
0 <= cost[i] <= 100
'''

# Time Complexity: O(N) where N is the length of cost due to iterating over the costs
# Space Complexity: O(1) due to using constant extra space (none)
def minCostClimbingStairs(cost: list[int]) -> int:
    for i in range(len(cost) - 3, -1, -1):
        cost[i] += min(cost[i + 1], cost[i + 2])

    return min(cost[0], cost[1])

# Test Cases
cost = [1,2,3]
assert minCostClimbingStairs(cost) == 2

cost = [1,2,1,2,1,1,1]
assert minCostClimbingStairs(cost) == 4