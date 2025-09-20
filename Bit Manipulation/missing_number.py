'''
Missing Number
Given an array nums containing n integers in the range [0, n] without any duplicates, return the single number in the range that is missing from nums.

Follow-up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

Constraints:

1 <= nums.length <= 1000
'''

def missingNumber(nums: list[int]) -> int:
    """
    Implement missingNumber
    """

# Test Cases
nums = [1,2,3]
assert missingNumber(nums) == 0

nums = [0,2]
assert missingNumber(nums) == 1