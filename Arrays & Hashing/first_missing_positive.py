'''
First Missing Positive
You are given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Constraints:

1 <= nums.length <= 100,000
-(2^31) <= nums[i] <= ((2^31)-1)
'''

def firstMissingPositive(nums: list[int]) -> int:
    """
    Implement firstMissingPositive
    """

# Test Cases
nums = [-2,-1,0]
assert firstMissingPositive(nums) == 1

nums = [1,2,4]
assert firstMissingPositive(nums) == 3

nums = [1,2,4,5,6,3,1]
assert firstMissingPositive(nums) == 7