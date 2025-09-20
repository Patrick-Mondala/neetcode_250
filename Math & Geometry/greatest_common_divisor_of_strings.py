'''
Greatest Common Divisor of Strings
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

You are given two strings str1 and str2, return the largest string x such that x divides both str1 and str2. If there is no such string, return "".

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
'''

def gcdOfStrings(str1: str, str2: str) -> str:
    """
    Implement gcdOfStrings
    """

# Test Cases
str1 = "ABAB"
str2 = "AB"
assert gcdOfStrings(str1, str2) == "AB"

str1 = "NANANA"
str2 = "NANA"
assert gcdOfStrings(str1, str2) == "NA"