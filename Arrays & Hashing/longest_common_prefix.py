'''
Longest Common Prefix
Solved 
You are given an array of strings strs. Return the longest common prefix of all the strings.

If there is no longest common prefix, return an empty string "".

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] is made up of lowercase English letters if it is non-empty.
'''

# Time Complexity: O(N * M) where N is the number of strings in strs and M is the length of the smallest string in strs
# Space Complexity: O(1)
def longestCommonPrefix(strs: list[str]) -> str:
    smallestStr = min(strs, key=len)

    for i in range(len(smallestStr)):
        for string in strs:
            if string[i] != smallestStr[i]:
                return smallestStr[:i]
    return smallestStr

# Test Cases
assert longestCommonPrefix(["flower","flow","flight"]) == "fl"
assert longestCommonPrefix(["dog","racecar","car"]) == ""
assert longestCommonPrefix(["bat","bag","bank","band"]) == "ba"
assert longestCommonPrefix(["dance","dag","danger","damage"]) == "da"
assert longestCommonPrefix(["neet","feet"]) == ""