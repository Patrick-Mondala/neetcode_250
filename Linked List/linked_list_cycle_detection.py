'''
Linked List Cycle Detection
Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.

Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

Note: index is not given to you as a parameter.

Constraints:

1 <= Length of the list <= 1000.
-1000 <= Node.val <= 1000
index is -1 or a valid index in the linked list.
'''
from linked_list_util import *

# Time Complexity: O(N) where N is the length of the linked list due to a slow pointer potentially reaching every node in the linked list
# Space Complexity: O(1) due to using constant space
def hasCycle(head: ListNode | None = None) -> bool:
    if not head:
        return False

    rabbit = hare = head

    while rabbit and rabbit.next and rabbit.next.next:
        rabbit = rabbit.next.next
        hare = hare.next
        if rabbit == hare:
            return True

    return False

# Test Cases
head = list_to_linked_list([1,2,3,4])
list_of_nodes = linked_list_to_list_of_nodes(head)
list_of_nodes[3].next = list_of_nodes[1]
assert hasCycle(head) == True

head = list_to_linked_list([1,2])
assert hasCycle(head) == False