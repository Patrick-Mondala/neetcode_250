'''
Same Binary Tree
Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

Constraints:

0 <= The number of nodes in both trees <= 100.
-100 <= Node.val <= 100
'''
from binary_tree_util import *

# Time Complexity: O(min(N, M)) where N is the size of tree p and M is the size of tree q due to DFSing over all the nodes of the smallest tree
# Space Complexity: O(min(N, M)) where N is the size of tree p and M is the size of tree q due to the recursive DFS calls adding to the call stack
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

# Test Cases
p = list_to_binary_tree([1,2,3])
q = list_to_binary_tree([1,2,3])
assert isSameTree(p, q) == True

p = list_to_binary_tree([4,7])
q = list_to_binary_tree([4,None,7])
assert isSameTree(p, q) == False

p = list_to_binary_tree([1,2,3])
q = list_to_binary_tree([1,3,2])
assert isSameTree(p, q) == False