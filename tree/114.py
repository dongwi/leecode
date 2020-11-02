from tree import TreeNode


class Solution:
    # flatten就是将每个子树的左右子树旋转
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return

        # 这里采用后序遍历
        self.flatten(root.left)
        self.flatten(root.right)

        # 找到之前的right节点
        prev_right = root.right
        root.right = root.left

        # 遍历到当前left节点的最后
        temp = root
        while temp.right:
            temp = temp.right
        temp.right = prev_right
