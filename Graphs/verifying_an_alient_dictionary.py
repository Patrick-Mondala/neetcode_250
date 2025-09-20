'''
Verifying An Alien Dictionary
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabets, return true if and only if the given words are sorted lexicographically in this alien language.

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
'''

def isAlienSorted(words: list[str], order: str) -> bool:
    """
    Implement isAlienSorted
    """

# Test Cases
words = ["dag","disk","dog"]
order = "hlabcdefgijkmnopqrstuvwxyz"
assert isAlienSorted(words, order) == True

words = ["neetcode","neet"]
order = "worldabcefghijkmnpqstuvxyz"
assert isAlienSorted(words, order) == False