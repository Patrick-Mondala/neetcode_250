'''
Baseball Game
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

Given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x: Record a new score of x.
'+': Record a new score that is the sum of the previous two scores.
'D': Record a new score that is the double of the previous score.
'C': Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

Note: The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

Constraints:

1 <= operations.length <= 1000
operations[i] is "C", "D", +, or a string representing an integer in the range [(-30,000), (30,000)].
For operation "+", there will always be at least two previous scores on the record.
For operations "C" and "D", there will always be at least one previous score on the record.
'''

def calPoints(operations: list[str]) -> int:
    stack = []

    for operation in operations:
        if operation == 'C':
            stack.pop()
        elif operation == 'D':
            stack.append(stack[-1] * 2)
        elif operation == '+':
            stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(operation))
    
    return sum(stack)

# Test Cases
assert calPoints(["1","2","+","C","5","D"]) == 18
assert calPoints(["5","D","+","C"]) == 15