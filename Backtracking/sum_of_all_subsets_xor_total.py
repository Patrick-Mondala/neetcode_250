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

# Time Complexity: O(2^N) where N is the size of nums, due to recursively iterating over each element in nums and branching between including or excluding it
# Space Complexity: O(N) where N is the size of nums, due to the recursive calls adding to the callstack with a max height of N
def subsetXORSum(nums: list[int]) -> int:
    def dfs(i, total):
        if i == len(nums):
            return total
        
        return dfs(i + 1, total ^ nums[i]) + dfs(i + 1, total)

    return dfs(0, 0)

# Test Cases
nums = [2,4]
assert subsetXORSum(nums) == 12

nums = [3,1,1]
assert subsetXORSum(nums) == 12