'''
Reverse Bits
Given a 32-bit unsigned integer n, reverse the bits of the binary representation of n and return the result.
'''

def reverseBits(n: int) -> int:
    """
    Implement reverseBits
    """

# Test Cases
n = int('00000000000000000000000000010101', 2)
assert reverseBits(n) == int('10101000000000000000000000000000', 2)