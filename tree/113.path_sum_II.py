"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

Return:
[
   [5,4,11,2],
   [5,8,4,5]
]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recursive
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root:
            return []

        res = []
        self.dfs(root, target, [], res)

        return res

    def dfs(
        self, node: TreeNode, target: int, path: List[int], res: List[List[int]]
    ) -> None:
        if node.val == target and not node.left and not node.right:
            path.append(node.val)
            res.append(path)

        if node.left:
            self.dfs(node.left, target - node.val, path + [node.val], res)

        if node.right:
            self.dfs(node.right, target - node.val, path + [node.val], res)


# Solution 2: iterative
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root:
            return []

        stk = [(root, target, [])]
        res = []

        while stk:
            node, val, path = stk.pop()

            if node:
                if val == node.val and not node.left and not node.right:
                    res.append(path + [node.val])
                else:
                    stk.append((node.left, val - node.val, path + [node.val]))
                    stk.append((node.right, val - node.val, path + [node.val]))

        return res
