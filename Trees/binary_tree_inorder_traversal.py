'''
Binary Tree Inorder Traversal
You are given the root of a binary tree, return the inorder traversal of its nodes' values.

Constraints:

0 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100
Follow up: Recursive solution is trivial, could you do it iteratively?
'''

from binary_tree_util import *

# Time Complexity: O(N) where N is the size of the tree due to making a single pass over all nodes in the tree
# Space Complexity: O(N) where N is the size of the tree due to each recursive call to traverse the tree will be added to the callstack potentially to size N
def inorderTraversal(root: TreeNode | None = None) -> list[int]:
    res = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)

    dfs(root)
    return res

# Test Cases
root = list_to_binary_tree([1,2,3,4,5,6,7])
assert inorderTraversal(root) == [4,2,5,1,6,3,7]

root = list_to_binary_tree([1,2,3,None,4,5,None])
assert inorderTraversal(root) == [2,4,1,5,3]

root = None
assert inorderTraversal(root) == []