class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class NotBalanceException(Exception):
    pass

# 这个与计算二叉树的深度的题目相似
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(r: TreeNode):
            if not r:
                return 0
            # 分别计算两个子树的高度
            left_height = helper(r.left)
            right_height = helper(r.right)

            # 如果子树的高度差小于2，则说明是平衡的。并返回当前节点的高度
            if abs(left_height - right_height) < 2:
                return max(left_height, right_height) + 1
            else:
                # 非平衡，则抛出异常
                raise NotBalanceException()
        try:
            helper(root)
            return True
        except NotBalanceException:
            return False
