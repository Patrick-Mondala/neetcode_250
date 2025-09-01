class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked_list(arr: list) -> ListNode:
    prev = None
    head = None

    for val in arr:
        cur = ListNode(val)
        if prev:
            prev.next = cur
        else:
            head = cur
        prev = cur

    return head

def linked_list_to_list(head: ListNode | None = None) -> list:
    res = []
    cur = head

    while cur:
        res.append(cur.val)
        cur = cur.next

    return res

def linked_list_to_list_of_nodes(head: ListNode | None = None) -> list:
    res = []
    cur = head

    while cur:
        res.append(cur)
        cur = cur.next

    return res