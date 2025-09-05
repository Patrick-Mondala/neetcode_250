'''
Binary Tree Preorder Traversal
You are given the root of a binary tree, return the preorder traversal of its nodes' values.

Constraints:

0 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100
Follow up: Recursive solution is trivial, could you do it iteratively?
'''
from binary_tree_util import *

# Time Complexity: O(N) where N is the size of the tree due to DFSing once through the entire tree
# Space Complexity: O(N) where N is the size of the tree due to recursive calls adding to call stack size
def preorderTraversal(root: list[TreeNode]) -> list[int]:
    res = []

    def dfs(node):
        if not node:
            return
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return res

# Test Cases
root = list_to_binary_tree([1,2,3,4,5,6,7])
assert preorderTraversal(root) == [1,2,4,5,3,6,7]

root = list_to_binary_tree([1,2,3,None,4,5,None])
assert preorderTraversal(root) == [1,2,4,3,5]

root = None
assert preorderTraversal(root) == []