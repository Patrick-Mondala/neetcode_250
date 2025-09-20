'''
Climbing Stairs
You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.

Return the number of distinct ways to climb to the top of the staircase.

Constraints:

1 <= n <= 30
'''

def climbStairs(n: int) -> int:
    """
    Implement climbStairs
    """

# Test Cases
n = 2
assert climbStairs(n) == 2

n = 3
assert climbStairs(n) == 3