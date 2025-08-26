'''
Valid Palindrome II
You are given a string s, return true if the s can be a palindrome after deleting at most one character from it.

A palindrome is a string that reads the same forward and backward.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Constraints:

1 <= s.length <= 100,000
s is made up of only lowercase English letters.
'''

# Time Complexity: O(N) where N is the length of s because we iterate over s at most 3 times
# Space Complexity: O(1) because we are using a constant amount of extra space, at most 2 calls in callstack
def validPalindrome(s: str, deleted: int | None=None) -> bool:
    l, r = 0, len(s) - 1
    
    while l < r:
        if l == deleted:
            l += 1
        if r == deleted:
            r -= 1
        if s[l] != s[r]:
            if deleted:
                return False
            return validPalindrome(s, l) or validPalindrome(s, r)
        l += 1
        r -= 1

    return True

# Test Cases
assert validPalindrome('aca') == True
assert validPalindrome('abbadc') == False
assert validPalindrome('abbda') == True