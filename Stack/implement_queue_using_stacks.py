'''
Implement Queue using Stacks
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.
Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.
'''

# Time Complexity: O(1) due to using constant time for each operation
# Space Complexity: O(1) due to using constant space to store the data. technically O(100) due to using an array of size 100 to store data with max 100 calls
class MyQueue:
    def __init__(self):
        self.stack = [None for _ in range(100)]
        self.head = self.tail = -1

    def push(self, x: int) -> None:
        self.stack[self.tail + 1] = x
        self.tail += 1

    def pop(self) -> int:
        if self.head == self.tail:
            return
        val = self.stack[self.head + 1]
        self.stack[self.head + 1] = None
        self.head += 1
        return val

    def peek(self) -> int:
        if self.head == self.tail:
            return
        return self.stack[self.head + 1]

    def empty(self) -> bool:
        return self.head == self.tail
    
# Test Cases
queue = MyQueue()
assert queue.push(1) == None
assert queue.push(2) == None
assert queue.peek() == 1
assert queue.pop() == 1
assert queue.empty() == False