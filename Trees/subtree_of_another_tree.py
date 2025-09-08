'''
Subtree of Another Tree
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Constraints:

1 <= The number of nodes in both trees <= 100.
-100 <= root.val, subRoot.val <= 100
'''
from binary_tree_util import *

# Time Complexity: O(N * M) where N is the size of the root tree and M is the size of the subroot tree,
# due to potentially DFSing over the subroot tree for every node in the root tree
# Space Complexity: O(N + M) where N is the size of the root tree and M is the size of the subroot tree,
# due to potentially DFSing the subroot tree at the bottom of the root tree, causing N + M recursive calls in the callstack
def isSubtree(root: TreeNode | None = None, subRoot: TreeNode | None = None) -> bool:
    def isSameTree(p: TreeNode | None = None, q: TreeNode | None = None) -> bool:
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            
            return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)

        return dfs(p, q)
    
    def dfs2(node):
        if not node:
            return False
        
        if node.val == subRoot.val:
            if isSameTree(node, subRoot):
                return True
        return dfs2(node.left) or dfs2(node.right)

    return dfs2(root)

# Test Cases
root = list_to_binary_tree([1,2,3,4,5])
subRoot = list_to_binary_tree([2,4,5])
assert isSubtree(root, subRoot) == True

root = list_to_binary_tree([1,2,3,4,5,None,None,6])
subRoot = list_to_binary_tree([2,4,5])
assert isSubtree(root, subRoot) == False