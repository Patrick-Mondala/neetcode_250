'''
Single Number
You are given a non-empty array of integers nums. Every integer appears twice except for one.

Return the integer that appears only once.

You must implement a solution with 
O(n) runtime complexity and use only 
O(1) extra space.

Constraints:

1 <= nums.length <= 10000
-10000 <= nums[i] <= 10000
'''

def singleNumber(nums: list[int]) -> int:
    """
    Implement singleNumber
    """

# Test Cases
nums = [3,2,3]
assert singleNumber(nums) == 2

nums = [7,6,6,7,8]
assert singleNumber(nums) == 8