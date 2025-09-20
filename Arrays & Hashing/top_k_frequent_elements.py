'''
Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.
'''

def topKFrequent(nums: list[int], k: int) -> list[int]:
    """
    Implement topKFrequent
    """

# Test Cases
nums = [1,2,2,3,3,3]
k = 2
assert topKFrequent(nums, k) == [2,3]


nums = [7,7]
k = 1
assert topKFrequent(nums, k) == [7]