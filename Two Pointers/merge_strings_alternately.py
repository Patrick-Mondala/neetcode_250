'''
Merge Strings Alternately
You are given two strings, word1 and word2. Construct a new string by merging them in alternating order, starting with word1 — take one character from word1, then one from word2, and repeat this process.

If one string is longer than the other, append the remaining characters from the longer string to the end of the merged result.

Return the final merged string.

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
'''

# Time Complexity: O(max(N, M)) where N is the length of word1 and M is the length of word2 due to iterating at most the length of the longest word times
# Space Complexity: O(N + M) due to storing a result array containing all elements of word1 and word2
def mergeAlternately(word1: str, word2: str) -> str:
    res = []

    N = len(max((word1, word2), key=len))

    for i in range(N):
        if i < len(word1):
            res.append(word1[i])
        if i < len(word2):
            res.append(word2[i])

    return ''.join(res)

# Test Cases
assert mergeAlternately("abc", "xyz") == "axbycz"
assert mergeAlternately("ab", "abbxxc") == "aabbbxxc"