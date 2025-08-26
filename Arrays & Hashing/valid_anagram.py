'''
Valid Anagram
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
'''

# Time Complexity: O(N + M) where N is the length of the strings s and M is the length of the string t
# Space Complexity: O(1) since the frequency map will at most contain 26 key-value pairs for each letter in the English alphabet
def isAnagram(s: str, t: str) -> bool:
    freq = [0] * 26  # Frequency map for each letter in the English alphabet

    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        freq[ord(s[i]) - ord('a')] += 1
        freq[ord(t[i]) - ord('a')] -= 1

    return all(count == 0 for count in freq)

# Test cases
assert isAnagram("racecar", "carrace") == True
assert isAnagram("jar", "jam") == False