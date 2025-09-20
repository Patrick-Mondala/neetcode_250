'''
Encode and Decode Strings
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
'''

def encode(strs: list[str]) -> str:
    """
    Implement encode
    """

def decode(s: str) -> list[str]:
    """
    Implement decode
    """

# Test Cases
arr = ["neet","code","love","you"]
assert decode(encode(arr)) == arr

arr = ["we","say",":","yes"]
assert decode(encode(arr)) == arr