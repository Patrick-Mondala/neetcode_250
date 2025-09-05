'''
Binary Tree Postorder Traversal
You are given the root of a binary tree, return the postorder traversal of its nodes' values.

Constraints:

0 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100
Follow up: Recursive solution is trivial, could you do it iteratively?
'''

from binary_tree_util import *

# Time Complexity: O(N) where N is the size of the tree due to iterating over the tree and reversing the results array
# Space Complexity: O(1) due to using constant space
def postorderTraversal(root: TreeNode | None = None) -> list[int]:
    res = []
    cur = root

    while cur:
        if not cur.right:
            res.append(cur.val)
            cur = cur.left
        else:
            prev = cur.right
            while prev.left and prev.left != cur:
                prev = prev.left

            if not prev.left:
                res.append(cur.val)
                prev.left = cur
                cur = cur.right
            else:
                prev.left = None
                cur = cur.left

    res.reverse()
    return res

# Test Cases
root = list_to_binary_tree([1,2,3,4,5,6,7])
assert postorderTraversal(root) == [4,5,2,6,7,3,1]

root = list_to_binary_tree([1,2,3,None,4,5,None])
assert postorderTraversal(root) == [4,2,5,3,1]

root = None
assert postorderTraversal(root) == []