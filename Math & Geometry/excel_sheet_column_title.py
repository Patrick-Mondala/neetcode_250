'''
Excel Sheet Column Title
You are given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Constraints:

1 <= columnNumber <= ((2^31)-1)
'''

def convertToTitle(columnNumber: int) -> str:
    """
    Implement convertToTitle
    """

# Test Cases
columnNumber = 32
assert convertToTitle(columnNumber) == "AF"

columnNumber = 53
assert convertToTitle(columnNumber) == "BA"