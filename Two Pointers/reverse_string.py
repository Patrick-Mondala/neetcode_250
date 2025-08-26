'''
Reverse String
You are given an array of characters which represents a string s. Write a function which reverses a string.

You must do this by modifying the input array in-place with O(1) extra memory.

Constraints:

0 <= s.length < 100,000
s[i] is a printable ascii character.
'''

# Time Complexity: O(N) where N is the length of s due to making a single pass over the s array
# Space Complexity: O(1) because we don't store data in any datastructures
def reverseString(s: list[str]) -> None:
    N = len(s)

    for i in range(N // 2):
        s[i], s[N - 1 - i] = s[N - 1 - i], s[i]

# Test Cases
s = ["n","e","e","t"]
reverseString(s)
assert s == ["t","e","e","n"]
s = ["r","a","c","e","c","a","r"]
reverseString(s)
assert s == ["r","a","c","e","c","a","r"]