'''
Subarray Sum Equals K
You are given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:

1 <= nums.length <= 20,000
-1,000 <= nums[i] <= 1,000
-10,000,000 <= k <= 10,000,000
'''

def subarraySum(nums: list[int], k: int) -> int:
    """
    Implement subarraySum
    """

# Test Cases
nums = [2,-1,1,2]
k = 2
assert subarraySum(nums, k) == 4

nums = [4,4,4,4,4,4]
k = 4
assert subarraySum(nums, k) == 6