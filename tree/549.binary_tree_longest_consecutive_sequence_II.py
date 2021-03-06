"""
Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.
Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:
Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
 
Example 2:
Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
 
Note: All the values of tree nodes are in the range of [-1e7, 1e7].
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = [0]
        self.dfs(root, res)

        return res[0]

    def dfs(self, node: TreeNode, res: List[int]) -> List[int]:
        if not node:
            return [0, 0]

        inc = dec = 1
        left = self.dfs(node.left, res)
        right = self.dfs(node.right, res)

        if node.left:
            if node.left.val == node.val + 1:
                inc = max(inc, left[0] + 1)
            if node.left.val == node.val - 1:
                dec = max(dec, left[1] + 1)

        if node.right:
            if node.right.val == node.val + 1:
                inc = max(inc, right[0] + 1)
            if node.right.val == node.val - 1:
                dec = max(dec, right[1] + 1)

        res[0] = max(res[0], inc + dec - 1)

        return [inc, dec]
