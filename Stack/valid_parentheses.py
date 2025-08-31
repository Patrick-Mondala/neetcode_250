'''
Valid Parentheses
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Constraints:

1 <= s.length <= 1000
'''

# Time Complexity: O(N) where N is the length of s due to iterating over the characters in s once
# Space Complexity: O(N) where N is the length of s due to potentially storing all characters in s into the stack
def isValid(s: str) -> bool:
    stack = []
    openersByClosers = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for cur in s:
        if cur in openersByClosers:
            if stack and stack.pop() == openersByClosers[cur]:
                continue
            return False
        stack.append(cur)

    return not stack

# Test Cases
assert isValid("[]") == True
assert isValid("[(])") == False