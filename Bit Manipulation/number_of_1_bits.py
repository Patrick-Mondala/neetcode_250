'''
Number of One Bits
You are given an unsigned integer n. Return the number of 1 bits in its binary representation.

You may assume n is a non-negative integer which fits within 32-bits.
'''

def hammingWeight(n: int) -> int:
    """
    Implement hammingWeight
    """

# Test Cases
n = int('00000000000000000000000000010111', 2)
assert hammingWeight(n) == 4

n = int('01111111111111111111111111111101', 2)
assert hammingWeight(n) == 30