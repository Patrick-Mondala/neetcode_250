'''
Sqrt(x)
You are given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Constraints:

0 <= x <= ((2^31)-1)
'''

# Time Complexity: O(logN) where N is the value of x
# Space Complexity: O(1) due to using constant extra space
def mySqrt(x: int) -> int:
    l, r = 0, x

    while l <= r:
        mid = l + ((r - l) // 2)
        if mid * mid == x:
            return mid
        if mid * mid < x:
            l = mid + 1
        else:
            r = mid - 1

    return r

# Test Cases
assert mySqrt(9) == 3
assert mySqrt(13) == 3