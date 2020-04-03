"""
Given a binary tree, return the sum of values of its deepest leaves.

Example 1:
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Constraints:
The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recursive
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        res = [0]
        max_depth = [0]
        self.dfs(root, 0, max_depth, res)

        return res[0]

    def dfs(
        self, root: TreeNode, cur_depth: int, max_depth: List[int], res: List[int]
    ) -> None:
        if not root:
            return

        if not root.left and not root.right:
            if cur_depth > max_depth[0]:
                res[0] = root.val
                max_depth[0] = cur_depth
            elif cur_depth == max_depth[0]:
                res[0] += root.val

        self.dfs(root.left, cur_depth + 1, max_depth, res)
        self.dfs(root.right, cur_depth + 1, max_depth, res)


# Solution 2: iterative
from collections import deque


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = deque([root])

        while q:
            res = 0

            for _ in range(len(q)):
                node = q.popleft()
                res += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return res
