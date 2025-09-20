'''
Counting Bits
Given an integer n, count the number of 1's in the binary representation of every number in the range [0, n].

Return an array output where output[i] is the number of 1's in the binary representation of i.

Constraints:

0 <= n <= 1000
'''

def countBits(n: int) -> list[int]:
    """
    Implement countBits
    """

# Test Cases
n = 4
assert countBits(n) == [0,1,1,2,1]