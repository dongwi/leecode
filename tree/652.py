from tree import TreeNode
from typing import List


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        node_tree = []
        def helper(node: TreeNode):
            # 采用后序遍历的方式
            helper(node.left)
            helper(node.right)


