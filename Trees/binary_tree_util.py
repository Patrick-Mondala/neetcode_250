class TreeNode:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_to_list_notation(root: TreeNode | None = None) -> list[int]:
    if not root:
        return []

    res = []
    queue = MyQueue()
    queue.push(root)
    real_nodes = 1

    while queue and real_nodes:
        cur = queue.pop()
        res.append(cur.val)

        if cur.val:
            real_nodes -= 1

        if cur.left:
            queue.push(cur.left)
            real_nodes += 1
        else:
            queue.push(TreeNode())

        if cur.right:
            queue.push(cur.right)
            real_nodes += 1
        else:
            queue.push(TreeNode())

    return res

def list_to_list_of_tree_nodes(arr: list | None = None) -> list[TreeNode]:
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

def list_to_binary_tree(arr: list[int] | None = None) -> TreeNode | None:
    if not arr:
        return
    return list_to_list_of_tree_nodes(arr)[0]

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: TreeNode) -> None:
        self.stack1.append(x)

    def pop(self) -> TreeNode:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> TreeNode:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2