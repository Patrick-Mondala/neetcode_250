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

# Time Complexity: O(N + C) where N is the length of words due to iterating over the words list, and C is the total characters in words due to iterating over every character in each word
# Space Complexity: O(1) due to using constant extra space (a dictionary of size 26)
def isAlienSorted(words: list[str], order: str) -> bool:
    alien_ord = {char: i for i, char in enumerate(order)}

    for i in range(1, len(words)):
        word = words[i]
        prev_word = words[i - 1]
        
        if get_word_value(word, alien_ord) < get_word_value(prev_word, alien_ord):
            return False
    
    return True


def get_word_value(word: str, alien_ord: dict) -> int:
        res = 0

        counter = 100
        for char in word:
            res += alien_ord[char] * (10 ** counter)
            counter -= 1

        return res

# Test Cases
words = ["dag","disk","dog"]
order = "hlabcdefgijkmnopqrstuvwxyz"
assert isAlienSorted(words, order) == True

words = ["neetcode","neet"]
order = "worldabcefghijkmnpqstuvxyz"
assert isAlienSorted(words, order) == False