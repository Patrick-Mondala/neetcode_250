'''
Valid Anagram
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
'''

# Time Complexity: O(N + M) where N is the length of the strings s and M is the length of the string t
# Space Complexity: O(1) since the frequency map will at most contain 26 key-value pairs for each letter in the English alphabet
def isAnagram(s: str, t: str) -> bool:
    freqMap = {}

    for char in s:
        if char not in freqMap:
            freqMap[char] = 0
        freqMap[char] += 1
    
    for char in t:
        if char not in freqMap:
            return False
        if freqMap[char] == 0:
            return False
        freqMap[char] -= 1
    
    for char, count in freqMap.items():
        if count != 0:
            return False
    
    return True

# Test cases
assert isAnagram("racecar", "carrace") == True
assert isAnagram("jar", "jam") == False