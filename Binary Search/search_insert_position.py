'''
Search Insert Position
You are given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Constraints:

1 <= nums.length <= 10,000.
-10,000 < nums[i], target < 10,000
nums contains distinct values sorted in ascending order.
'''

import bisect

# Time Complexity: O(logN) where N is the length of nums
# Space Complexity: O(1) due to using constant extra space
def searchInsert(nums: list[int], target: int) -> int:
    res = bisect.bisect_left(nums, target)
    return res

# Test Cases
assert searchInsert([-1,0,2,4,6,8], 5) == 4
assert searchInsert([-1,0,2,4,6,8], 10) == 6