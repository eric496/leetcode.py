"""
Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.
Two trees are duplicate if they have the same structure with same node values.

Example 1:
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:
      2
     /
    4
and
    4
Therefore, you need to return above trees' root in the form of a list.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        res = []
        self.dfs(root, {}, res)

        return res

    def dfs(self, node: TreeNode, cnt: dict, res: List[TreeNode]) -> str:
        if not node:
            return ""

        s = (
            "("
            + self.dfs(node.left, cnt, res)
            + str(node.val)
            + self.dfs(node.right, cnt, res)
            + ")"
        )

        if cnt.get(s, 0) == 1:
            res.append(node)

        cnt[s] = cnt.get(s, 0) + 1

        return s
