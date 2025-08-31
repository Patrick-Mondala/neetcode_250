'''
Search Insert Position
You are given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Constraints:

1 <= nums.length <= 10,000.
-10,000 < nums[i], target < 10,000
nums contains distinct values sorted in ascending order.
'''

# Time Complexity: O(logN) where N is the length of nums
# Space Complexity: O(1) due to using constant extra space
def searchInsert(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = l + ((r - l) // 2)
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    
    return r + 1

# Test Cases
assert searchInsert([-1,0,2,4,6,8], 5) == 4
assert searchInsert([-1,0,2,4,6,8], 10) == 6