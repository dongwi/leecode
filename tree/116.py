class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self.connect_node(root.left, root.right)
        return root

    def connect_node(self, node1: 'Node', node2: 'Node'):
        if not node1 or not node2:
            return
        # 将节点链接在一起
        node1.next = node2
        # 相同父节点的左右节点
        self.connect_node(node1.left, node1.right)
        self.connect_node(node2.left, node2.right)
        # 不同父节点的左右节点
        self.connect_node(node1.right, node2.left)
