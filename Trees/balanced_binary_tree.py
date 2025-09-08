'''
Balanced Binary Tree
Given a binary tree, return true if it is height-balanced and false otherwise.

A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Constraints:

The number of nodes in the tree is in the range [0, 1000].
-1000 <= Node.val <= 1000
'''
from binary_tree_util import *

# Time Complexity: O(N) where N is the size of the binary tree due to DFSing over all the nodes
# Space Complexity: O(N) where N is the size of the binary tree due to recursive DFS calls potentially the same size of the tree
def isBalanced(root: TreeNode | None = None) -> bool:
    def dfs(node):
        if not node:
            return (True, 0)
        left = dfs(node.left)
        right = dfs(node.right)

        if not left[0] or not right[0]:
            return (False, 9999)

        return (abs(left[1] - right[1]) <= 1, max(left[1], right[1]) + 1)

    return dfs(root)[0]

# Test Cases
root = list_to_binary_tree([1,2,3,None,None,4])
assert isBalanced(root) == True

root = list_to_binary_tree([1,2,3,None,None,4,None,5])
assert isBalanced(root) == False

root = None
assert isBalanced(root) == True

root = list_to_binary_tree([1,2,2,3,None,None,3,4,None,None,4])
assert isBalanced(root) == False