# Definition for a binary tree node.
from tree import TreeNode

import collections


# BFS的遍历来计算depth
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        visited = set()
        q = collections.deque([root])
        visited.add(root)
        depth = 1
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if not cur.left and not cur.right:
                    return depth
                if cur.left and cur.left not in visited:
                    q.append(cur.left)
                    visited.add(cur.left)
                if cur.right and cur.right not in visited:
                    q.append(cur.right)
                    visited.add(cur.right)
            depth += 1
        return 0
