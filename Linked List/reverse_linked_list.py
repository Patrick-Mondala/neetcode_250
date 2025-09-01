'''
Reverse Linked List
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Constraints:

0 <= The length of the list <= 1000.
-1000 <= Node.val <= 1000
'''

from linked_list_util import ListNode, list_to_linked_list, linked_list_to_list

# Time Complexity: O(N) where N is the length of the linked list due to iterating over every node in the linked list
# Space Complexity: O(1) due to using constant extra space
def reverseList(head: ListNode | None = None) -> ListNode:
    cur = head
    prev = None

    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    return prev

# Test Cases
head = list_to_linked_list([0,1,2,3])
assert linked_list_to_list(reverseList(head)) == [3,2,1,0]


head = list_to_linked_list([])
assert linked_list_to_list(reverseList(head)) == []