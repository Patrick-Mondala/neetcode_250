'''
Extra Characters in a String
You are given a string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.

Note that the same word in the dictionary may be reused multiple times.

Constraints:

1 <= s.length <= 50
1 <= dictionary.length <= 50
1 <= dictionary[i].length <= 50
s and dictionary[i] consist of only lowercase English letters
dictionary contains distinct words
'''

def minExtraChar(s: str, dictionary: list[str]) -> int:
    """
    Implement minExtraChar
    """

# Test Cases
s = "neetcodes"
dictionary = ["neet","code","neetcode"]
assert minExtraChar(s, dictionary) == 1

s = "neetcodde"
dictionary = ["neet","code","neetcode"]
assert minExtraChar(s, dictionary) == 5