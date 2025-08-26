'''
Concatenation of Array
You are given an integer array nums of length n. Create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

Constraints:

1 <= nums.length <= 1000.
1 <= nums[i] <= 1000
'''

# Time Complexity: O(N) due to iteration through the nums array where N is the length of nums
# Space Complexity: O(N) due to creating an answer array of size 2N where N is the length of nums
def getConcatenation(nums: list[int]) -> list[int]:
    N = len(nums)
    ans = [None for _ in range(N * 2)]

    for i in range(N):
        ans[i] = nums[i]
        ans[i + N] = nums[i]

    return ans

# Test cases
assert getConcatenation([1,4,1,2]) == [1,4,1,2,1,4,1,2]
assert getConcatenation([22,21,20,1]) == [22,21,20,1,22,21,20,1]