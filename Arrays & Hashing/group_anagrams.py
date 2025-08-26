'''
Group Anagrams
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.
'''

# Time Complexity: O(N * M log M) where N is the number of strings in strs and M is the length of the longest string in strs
# Space Complexity: O(N * M) where N is the number of strings in strs and M is the length of the longest string in strs 
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    buckets = {} # sorted str, list[str]
    
    for i in range(len(strs)):
        sorted_str = ''.join(sorted(strs[i]))
        if sorted_str not in buckets:
            buckets[sorted_str] = []
        buckets[sorted_str].append(strs[i])

    return list(buckets.values())

# Test Cases
assert groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [["eat","tea","ate"],["tan","nat"],["bat"]]
assert groupAnagrams([""]) == [[""]]
assert groupAnagrams(["x"]) == [["x"]]