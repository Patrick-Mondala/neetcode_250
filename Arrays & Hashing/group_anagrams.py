from collections import defaultdict

'''
Group Anagrams
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.
'''

# Time Complexity: O(N * M) where N is the number of strings in strs and M is the length of the longest string in strs
# due to iterating through each string and creating a frequency map for each string
# Space Complexity: O(N * M) where N is the number of strings in strs and M is the length of the longest string in strs
# due to storing all strings in the frequency map
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    freqMaps = defaultdict(list) # (freqMap, list of anagrams)

    for string in strs:
        freqMap = [0] * 26

        for char in string:
            freqMap[ord(char) - ord('a')] += 1
        freqMaps[tuple(freqMap)].append(string)

    return list(freqMaps.values())

# Test Cases
assert groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [["eat","tea","ate"],["tan","nat"],["bat"]]
assert groupAnagrams([""]) == [[""]]
assert groupAnagrams(["x"]) == [["x"]]