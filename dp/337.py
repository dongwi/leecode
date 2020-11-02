from tree import TreeNode


class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                # 当前节点的偷，不偷
                return 0, 0
            left_val = helper(node.left)
            right_val = helper(node.right)
            # dfs的后序遍历，得到每个节点偷与不偷时的最高金额
            return node.val + left_val[1] + right_val[1], max(left_val) + max(right_val)

        return max(helper(root))

