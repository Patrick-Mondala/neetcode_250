'''
Kth Largest Element in a Stream
Design a class to find the kth largest integer in a stream of values, including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.

Implement the following methods:

constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.

Constraints:

1 <= k <= 1000
0 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-1000 <= val <= 1000
There will always be at least k integers in the stream when you search for the kth integer.
'''

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        """
        Implement KthLargest init
        """

    def add(self, val: int) -> int:
        """
        Implement add
        """

# Test Cases
kthLargest = KthLargest(3, [1, 2, 3, 3])
assert kthLargest.add(3) == 3
assert kthLargest.add(5) == 3
assert kthLargest.add(6) == 3
assert kthLargest.add(7) == 5
assert kthLargest.add(8) == 6