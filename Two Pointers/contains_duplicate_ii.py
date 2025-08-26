'''
Contains Duplicate II
You are given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k, otherwise return false.

Constraints:

1 <= nums.length <= 100,000
-1,000,000,000 <= nums[i] <= 1,000,000,000
0 <= k <= 100,000
'''

# Time Complexity: O(N) where N is the size of nums due to iterating over nums once
# Space Complexity: O(N) where N is the size of nums due to potentially storing every num in nums in the seen map
def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    seen = {}

    for i in range(len(nums)):
        if nums[i] in seen:
            if i - seen[nums[i]] <= k:
                return True
        seen[nums[i]] = i

    return False

# Test Cases
assert containsNearbyDuplicate(nums = [1,2,3,1], k = 3) == True
assert containsNearbyDuplicate(nums = [2,1,2], k = 1) == False