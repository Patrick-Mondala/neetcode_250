'''
Contains Duplicate II
You are given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k, otherwise return false.

Constraints:

1 <= nums.length <= 100,000
-1,000,000,000 <= nums[i] <= 1,000,000,000
0 <= k <= 100,000
'''

# Time Complexity: O(N) where N is the size of nums due to potentially iterating over the entire nums array
# Space Complexity: O(min(N, K)) where K is the maximum size of our seen set window
def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    seen = set()

    l, r = 0, 0

    while r < len(nums):
        if r - l > k:
            seen.remove(nums[l])
            l += 1
        if nums[r] in seen:
            return True
        seen.add(nums[r])
        r += 1

    return False

# Test Cases
assert containsNearbyDuplicate(nums = [1,2,3,1], k = 3) == True
assert containsNearbyDuplicate(nums = [2,1,2], k = 1) == False