from collections import defaultdict

'''
Majority Element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times in the array. You may assume that the majority element always exists in the array.

Constraints:

1 <= nums.length <= 50,000
-1,000,000,000 <= nums[i] <= 1,000,000,000
'''

# Boyer-Moore Voting Algorithm
# Time Complexity: O(N) where N is the length of nums due to single pass through nums array
# Space Complexity: O(1) since we are using only a constant amount of extra space
def majorityElement(nums: list[int]) -> int:
    count = 0
    majority = 0

    for num in nums:
        if count == 0:
            majority = num
        if majority == num:
            count += 1
        else:
            count -= 1
    
    return majority

# Test Cases
assert majorityElement([5,5,1,1,1,5,5]) == 5
assert majorityElement([2,2,2]) == 2