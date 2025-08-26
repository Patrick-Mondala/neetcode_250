'''
Valid Palindrome
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.
'''

# Time Complexity: O(N) where N is the length of s due to iterating over the characters in s once
# Space Complexity: O(1) since we are using a constant amount of extra space
def isPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while r > l and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1

    return True

# Test Cases
assert isPalindrome("Was it a car or a cat I saw?") == True
assert isPalindrome("tab a cat") == False