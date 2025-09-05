class TreeNode:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def list_to_list_of_tree_nodes(arr):
    res = []

    for val in arr:
        if not val:
            res.append(None)
        else:
            res.append(TreeNode(val))
    
    for i in range(len(arr) - 1, 0, -1):
        if res[i] == None:
            continue
        if i % 2 == 0:
            res[i // 2 - 1].right = res[i]
        else:
            res[i // 2].left = res[i]
    
    return res

def list_to_binary_tree(arr):
    if not arr:
        return
    return list_to_list_of_tree_nodes(arr)[0]