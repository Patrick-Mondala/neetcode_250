'''
Implement Stack Using Queues
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.
Follow-up: Can you implement the stack using only one queue?
'''

# Initialize Space Time Complexity: O(1) due to initialization only requiring constant extra space
# Push Space Time Complexity: O(1)
# Pop Space Time Complexity: O(1)
# Top Space Time Complexity: O(1)
# Empty Space Time Complexity: O(1)
class Node:
    def __init__(self, val = None, prev = None, nxt = None):
        self.val = val
        self.prev = prev
        self.nxt = nxt

class MyStack:
    def __init__(self):
        self.head = self.tail = Node()

    def push(self, x: int) -> None:
        self.tail.nxt = Node(x, self.tail)
        self.tail = self.tail.nxt

    def pop(self) -> int:
        if self.empty():
            return None
        res = self.tail.val
        self.tail.prev.nxt = None
        self.tail = self.tail.prev
        return res

    def top(self) -> int:
        return self.tail.val

    def empty(self) -> bool:
        return self.tail == self.head
    
# Test Cases
stack = MyStack()
assert stack.push(1) == None
assert stack.push(2) == None
assert stack.top() == 2
assert stack.pop() == 2
assert stack.empty() == False