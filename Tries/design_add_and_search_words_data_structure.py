'''
Design Add and Search Word Data Structure
Design a data structure that supports adding new words and searching for existing words.

Implement the WordDictionary class:

void addWord(word) Adds word to the data structure.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Constraints:

1 <= word.length <= 20
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 10,000 calls will be made to addWord and search.
'''

class WordDictionary:

    def __init__(self):
        """
        Implement WordDictionary init
        """

    def addWord(self, word: str) -> None:
        """
        Implement addWord
        """

    def search(self, word: str) -> bool:
        """
        Implement search
        """

wordDictionary = WordDictionary()
wordDictionary.addWord("day")
wordDictionary.addWord("bay")
wordDictionary.addWord("may")
assert wordDictionary.search("say") == False
assert wordDictionary.search("day") == True
assert wordDictionary.search(".ay") == True
assert wordDictionary.search("b..") == True