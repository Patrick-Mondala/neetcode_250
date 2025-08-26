'''
Contains Duplicate
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
'''

# Time Complexity: O(N) due to iteration through the nums array where N is the length of nums
# Space Complexity: O(N) due to creating a set to store seen elements where N is the length of nums
def hasDuplicate(nums: list[int]) -> bool:
    return len(set(nums)) != len(nums)

# Test cases
assert hasDuplicate([1, 2, 3, 3]) == True
assert hasDuplicate([1, 2, 3, 4]) == False