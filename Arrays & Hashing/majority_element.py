from collections import defaultdict

'''
Majority Element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times in the array. You may assume that the majority element always exists in the array.

Constraints:

1 <= nums.length <= 50,000
-1,000,000,000 <= nums[i] <= 1,000,000,000
'''

# Time Complexity: O(N) where N is the length of nums due to single pass through nums array
# Space Complexity: O(N) where N is the length of nums due to storing up to N key-value pairs in the frequency map
def majorityElement(nums: list[int]) -> int:
    freqMap = defaultdict(int)

    for num in nums:
        freqMap[num] += 1

    return max(freqMap, key=freqMap.get)

# Test Cases
assert majorityElement([5,5,1,1,1,5,5]) == 5
assert majorityElement([2,2,2]) == 2