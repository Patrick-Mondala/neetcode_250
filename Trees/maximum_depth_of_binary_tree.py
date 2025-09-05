'''
Maximum Depth of Binary Tree
Given the root of a binary tree, return its depth.

The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

Constraints:

0 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100
'''
from binary_tree_util import *

# Time Complexity: O(N) where N is the size of the binary tree due to DFSing over all the nodes in the tree
# Space Complexity: O(N) where N is the size of the binary tree due to the call stack size from recursive calls
def maxDepth(root: TreeNode | None = None) -> int:
    def dfs(node):
        if not node:
            return 0
        
        return max(dfs(node.left) + 1, dfs(node.right) + 1)
    
    return dfs(root)

# Test Cases
root = list_to_binary_tree([1,2,3,None,None,4])
assert maxDepth(root) == 3

root = None
assert maxDepth(root) == 0