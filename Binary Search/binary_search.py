'''
Binary Search
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in O(logn) time.

Constraints:

1 <= nums.length <= 10000.
-10000 < nums[i], target < 10000
All the integers in nums are unique.
'''

# Time Complexity: O(logN) where N is the length of nums due to doing logN iterations of our search, cutting our search space in half between iterations
# Space Complexity: O(1) due to using constant extra space
import bisect

def search(nums: list[int], target: int) -> int:
    res = bisect.bisect_left(nums, target)
    return res if res < len(nums) and nums[res] == target else -1

# Test Cases
assert search([-1,0,2,4,6,8], 4) == 3
assert search([-1,0,2,4,6,8], 3) == -1