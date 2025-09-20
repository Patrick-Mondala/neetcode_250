'''
N-th Tribonacci Number
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
'''

def tribonacci(n: int) -> int:
    """
    Implement tribonacci
    """

# Test Cases
n = 3
assert tribonacci(n) == 2

n = 21
assert tribonacci(n) == 121415