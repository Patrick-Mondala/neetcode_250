'''
Merge Two Sorted Linked Lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

Constraints:

0 <= The length of the each list <= 100.
-100 <= Node.val <= 100
'''

from linked_list_util import *

# Time Complexity: O(N + M) where N is the length of list1 and M is the length of list2 due to passing over both lists
# Space Complexity: O(1) due to merging the list in place
def mergeTwoLists(list1: ListNode | None = None, list2: ListNode | None = None) -> ListNode | None:
    cur1, cur2 = list1, list2
    sentinel = prev = ListNode()

    while cur1 and cur2:
        if cur1.val < cur2.val:
            prev.next = cur1
            cur1 = cur1.next
        else:
            prev.next = cur2
            cur2 = cur2.next
        prev = prev.next
    
    prev.next = cur1 or cur2

    return sentinel.next

# Test Cases
list1 = list_to_linked_list([1,2,4])
list2 = list_to_linked_list([1,3,5])
assert linked_list_to_list(mergeTwoLists(list1, list2)) == [1,1,2,3,4,5]

list1 = None
list2 = list_to_linked_list([1,2])
assert linked_list_to_list(mergeTwoLists(list1, list2)) == [1,2]

list1 = None
list2 = None
assert linked_list_to_list(mergeTwoLists(list1, list2)) == []