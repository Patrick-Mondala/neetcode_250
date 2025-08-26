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
# Space Complexity: O(M) where M is the length of the smallest string in strs due to storing the result array
def longestCommonPrefix(strs: list[str]) -> str:
    res = []
    smallestStr = min(strs, key=len)

    for i in range(len(smallestStr)):
        for string in strs:
            if string[i] != smallestStr[i]:
                return ''.join(res)
        res.append(string[i])
    return smallestStr

# Test Cases
assert longestCommonPrefix(None, ["flower","flow","flight"]) == "fl"
assert longestCommonPrefix(None, ["dog","racecar","car"]) == ""
assert longestCommonPrefix(None, ["bat","bag","bank","band"]) == "ba"
assert longestCommonPrefix(None, ["dance","dag","danger","damage"]) == "da"
assert longestCommonPrefix(None, ["neet","feet"]) == ""