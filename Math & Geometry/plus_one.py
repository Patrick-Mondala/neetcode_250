'''
Plus One
You are given an integer array digits, where each digits[i] is the ith digit of a large integer. It is ordered from most significant to least significant digit, and it will not contain any leading zero.

Return the digits of the given integer after incrementing it by one.

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
'''

def plusOne(digits: list[int]) -> list[int]:
    """
    Implement plusOne
    """

# Test Cases
digits = [1,2,3,4]
assert plusOne(digits) == [1,2,3,5]

digits = [9,9,9]
assert plusOne(digits) == [1,0,0,0]