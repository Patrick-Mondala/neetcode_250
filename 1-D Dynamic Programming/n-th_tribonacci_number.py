'''
N-th Tribonacci Number
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
'''

# Time Complexity: O(N) due to iterating from 3 up to N
# Space Complexity: O(1) due to using constant extra space
def tribonacci(n: int) -> int:
    t = [0, 1, 1]

    if n < 3:
        return t[n]

    for i in range(3, n + 1):
        t[i % 3] = sum(t)

    return t[n % 3]

# Test Cases
n = 3
assert tribonacci(n) == 2

n = 21
assert tribonacci(n) == 121415