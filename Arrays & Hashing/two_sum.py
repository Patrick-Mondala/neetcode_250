'''
Two Sum
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Constraints:

2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000
'''

# Time Complexity: O(N) where N is the length of nums due to single pass through nums array
# Space Complexity: O(N) where N is the length of nums due to storing up to N key-value pairs in the complement map
def twoSum(nums: list[int], target: int) -> list[int]:
    complementMap = {} # complement to target, index of original num

    for i in range(len(nums)):
        if nums[i] in complementMap:
            return [complementMap[nums[i]], i]
        complementMap[target - nums[i]] = i

# Test Cases
assert twoSum([3,4,5,6], 7) == [0,1]
assert twoSum([4,5,6], 10) == [0,2]
assert twoSum([5,5], 10) == [0,1]