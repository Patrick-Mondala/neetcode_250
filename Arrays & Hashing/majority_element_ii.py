'''
Majority Element II
You are given an integer array nums of size n, find all elements that appear more than ⌊ n/3 ⌋ times. You can return the result in any order.

Constraints:

1 <= nums.length <= 50,000.
-1,000,000,000 <= nums[i] <= 1,000,000,000
Follow up: Could you solve the problem in linear time and in O(1) space?
'''

def majorityElement(nums: list[int]) -> list[int]:
    """
    Implement majorityElement
    """

# Test Cases
nums = [5,2,3,2,2,2,2,5,5,5]
assert majorityElement(nums) == [2,5]

nums = [4,4,4,4,4]
assert majorityElement(nums) == [4]

nums = [1,2,3]
assert majorityElement(nums) == []