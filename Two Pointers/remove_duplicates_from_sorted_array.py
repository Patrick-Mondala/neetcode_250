'''
Remove Duplicates From Sorted Array
You are given an integer array nums sorted in non-decreasing order. Your task is to remove duplicates from nums in-place so that each element appears only once.

After removing the duplicates, return the number of unique elements, denoted as k, such that the first k elements of nums contain the unique elements.

Note:

The order of the unique elements should remain the same as in the original array.
It is not necessary to consider elements beyond the first k positions of the array.
To be accepted, the first k elements of nums must contain all the unique elements.
Return k as the final result.

Constraints:

1 <= nums.length <= 30,000
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
'''

# Time Complexity: O(N) where N is the length of nums due to making a single pass over the nums array
# Space Complexity: O(1) due to using constant extra space to store a pointer
def removeDuplicates(nums: list[int]) -> int:
    pointer = 1 # placement pointer

    for i in range(1, len(nums)):
        if pointer >= len(nums):
            break
        if nums[i] == nums[pointer - 1]:
            continue
        nums[pointer] = nums[i]
        pointer += 1

    return pointer

# Test Cases
nums = [1,1,2,3,4]
assert removeDuplicates(nums) == 4
assert nums[:4] == [1,2,3,4]

nums = [2,10,10,30,30,30]
assert removeDuplicates(nums) == 3
assert nums[:3] == [2,10,30]