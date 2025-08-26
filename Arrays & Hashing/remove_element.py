'''
Remove Element
You are given an integer array nums and an integer val. Your task is to remove all occurrences of val from nums in-place.

After removing all occurrences of val, return the number of remaining elements, say k, such that the first k elements of nums do not contain val.

Note:

The order of the elements which are not equal to val does not matter.
It is not necessary to consider elements beyond the first k positions of the array.
To be accepted, the first k elements of nums must contain only elements not equal to val.
Return k as the final result.

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
'''

# Time Complexity: O(N) where N is the length of nums due to single pass through nums array
# Space Complexity: O(1) since we are modifying the input array in place
def removeElement(nums: list[int], val: int) -> int:
    k = len(nums)
    pointer = 0

    for i in range(len(nums)):
        if nums[i] == val:
            k -= 1
            continue
        nums[pointer], nums[i] = nums[i], nums[pointer]
        pointer += 1

    return k

# Test Cases
nums = [1,1,2,3,4]
assert removeElement(nums, 1) == 3
assert nums[:3] == [2,3,4]
nums = [0,1,2,2,3,0,4,2]
assert removeElement(nums, 2) == 5
assert nums[:5] == [0,1,3,0,4]