'''
Climbing Stairs
You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.

Return the number of distinct ways to climb to the top of the staircase.

Constraints:

1 <= n <= 30
'''

# Time Complexity: O(N) where N is how many stairs there are, due to iterating from 3 up to N
# Space Complexity: O(1) due to using constant extra space
def climbStairs(n: int) -> int:
    prev = 2
    prev_prev = 1
    
    for _ in range(3, n + 1):
        temp = prev + prev_prev
        prev_prev = prev
        prev = temp

    return prev

# Test Cases
n = 2
assert climbStairs(n) == 2

n = 3
assert climbStairs(n) == 3