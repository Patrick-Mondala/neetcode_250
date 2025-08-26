'''
Merge Sorted Array
You are given two integer arrays nums1 and nums2, both sorted in non-decreasing order, along with two integers m and n, where:

m is the number of valid elements in nums1,
n is the number of elements in nums2.
The array nums1 has a total length of (m+n), with the first m elements containing the values to be merged, and the last n elements set to 0 as placeholders.

Your task is to merge the two arrays such that the final merged array is also sorted in non-decreasing order and stored entirely within nums1.
You must modify nums1 in-place and do not return anything from the function.

Constraints:

0 <= m, n <= 200
1 <= (m + n) <= 200
nums1.length == (m + n)
nums2.length == n
-1,000,000,000 <= nums1[i], nums2[i] <= 1,000,000,000
'''

# Time Complexity: O(N) where N is the length of nums1 due to iterating N times to populate the nums1 array
# Space Complexity: O(1) due to using constant extra space
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    # shift nums1 to the right
    for i in range(m - 1, -1, -1):
        nums1[i], nums1[i + n] = nums1[i + n], nums1[i]

    pp = 0 # placement pointer
    p1 = n # nums1 pointer
    p2 = 0 # num2 pointer

    while pp < len(nums1):
        if p2 >= len(nums2) or p1 < len(nums1) and nums1[p1] <= nums2[p2]:
            nums1[pp] = nums1[p1]
            p1 += 1
        else:
            nums1[pp] = nums2[p2]
            p2 += 1
        pp += 1

# Test Cases
nums1 = [10,20,20,40,0,0]
m = 4
nums2 = [1,2]
n = 2
merge(nums1, m, nums2, n)
assert nums1 == [1,2,10,20,20,40]

nums1 = [0,0]
m = 0
nums2 = [1,2]
n = 2
merge(nums1, m, nums2, n)
assert nums1 == [1,2]