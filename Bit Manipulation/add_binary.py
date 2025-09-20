'''
Add Binary
You are given two binary strings a and b, return their sum as a binary string.

Constraints:

1 <= a.length, b.length <= 10,000
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''

def addBinary(a: str, b: str) -> str:
    """
    Implement addBinary
    """

# Test Cases
a = "101"
b = "10"
assert addBinary(a, b) == "111"

a = "10010"
b = "111"
assert addBinary(a, b) == "11001"