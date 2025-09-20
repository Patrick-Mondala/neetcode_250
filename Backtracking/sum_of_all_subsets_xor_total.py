'''
Sum of All Subsets XOR Total
The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
You are given an array nums, return the sum of all XOR totals for every subset of nums.

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

Constraints:

1 <= nums.length <= 12
1 <= nums[i] <= 20
'''

def subsetXORSum(nums: list[int]) -> int:
    """
    Implement subsetXORSum
    """

# Test Cases
nums = [2,4]
assert subsetXORSum(nums) == 12

nums = [3,1,1]
assert subsetXORSum(nums) == 12