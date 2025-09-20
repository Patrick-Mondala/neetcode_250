'''
Sort an Array
You are given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

Constraints:

1 <= nums.length <= 50,000.
-50,000 <= nums[i] <= 50,000
'''

def sortArray(nums: list[int]) -> list[int]:
    """
    Implement sortArray
    """


# Test Cases
nums = [10,9,1,1,1,2,3,1]
assert sortArray(nums) == [1,1,1,1,2,3,9,10]

nums = [5,10,2,1,3]
assert sortArray(nums) == [1,2,3,5,10]