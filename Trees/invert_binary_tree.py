'''
Invert Binary Tree
You are given the root of a binary tree root. Invert the binary tree and return its root.

Constraints:

0 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100
'''
from binary_tree_util import *

def invertTree(root: TreeNode | None = None) -> TreeNode | None:
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        node.left, node.right = node.right, node.left
    
    dfs(root)
    return root

# Test Cases
root = list_to_binary_tree([1,2,3,4,5,6,7])
assert binary_tree_to_list_notation(invertTree(root)) == [1,3,2,7,6,5,4]

root = list_to_binary_tree([3,2,1])
assert binary_tree_to_list_notation(invertTree(root)) == [3,1,2]

root = None
assert binary_tree_to_list_notation(invertTree(root)) == []