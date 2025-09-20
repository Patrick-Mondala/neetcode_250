'''
Products of Array Except Self
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O(n) time without using the division operation?

Constraints:

2 <= nums.length <= 1000
-20 <= nums[i] <= 20
'''

def productExceptSelf(nums: list[int]) -> list[int]:
    """
    Implement productExceptSelf
    """

# Test Cases
nums = [1,2,4,6]
assert productExceptSelf(nums) == [48,24,12,8]

nums = [-1,0,1,2,3]
assert productExceptSelf(nums) == [0,-6,0,0,0]