'''
Implement Trie (Prefix Tree)
A prefix tree (also known as a trie) is a tree data structure used to efficiently store and retrieve keys in a set of strings. Some applications of this data structure include auto-complete and spell checker systems.

Implement the PrefixTree class:

PrefixTree() Initializes the prefix tree object.
void insert(String word) Inserts the string word into the prefix tree.
boolean search(String word) Returns true if the string word is in the prefix tree (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Constraints:

1 <= word.length, prefix.length <= 1000
word and prefix are made up of lowercase English letters.
'''

class PrefixTree:

    def __init__(self):
        """
        Implement PrefixTree init
        """

    def insert(self, word: str) -> None:
        """
        Implement insert
        """

    def search(self, word: str) -> bool:
        """
        Implement search
        """

    def startsWith(self, prefix: str) -> bool:
        """
        Implement startsWith
        """

# Test Cases
prefixTree = PrefixTree()
prefixTree.insert("dog")
assert prefixTree.search("dog") == True
assert prefixTree.search("do") == False
assert prefixTree.startsWith("do") == True
assert prefixTree.insert("do")
assert prefixTree.search("do") == True