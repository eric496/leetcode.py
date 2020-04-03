"""
Given a binary tree with N nodes, each node has a different value from {1, ..., N}.
A node in this binary tree can be flipped by swapping the left child and the right child of that node.
Consider the sequence of N values reported by a preorder traversal starting from the root.  Call such a sequence of N values the voyage of the tree.
(Recall that a preorder traversal of a node means we report the current node's value, then preorder-traverse the left child, then preorder-traverse the right child.)
Our goal is to flip the least number of nodes in the tree so that the voyage of the tree matches the voyage we are given.
If we can do so, then return a list of the values of all nodes flipped.  You may return the answer in any order.
If we cannot do so, then return the list [-1].

Example 1:
Input: root = [1,2], voyage = [2,1]
Output: [-1]

Example 2:
Input: root = [1,2,3], voyage = [1,3,2]
Output: [1]

Example 3:
Input: root = [1,2,3], voyage = [1,2,3]
Output: []

Note:
1 <= N <= 100
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recursive
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        res = []

        return res if self.dfs(root, voyage[::-1], res) else [-1]

    def dfs(self, node: TreeNode, voyage: List[int], res: List[int]) -> bool:
        if not node:
            return True

        if node.val != voyage.pop():
            return False

        if node.left and node.left.val != voyage[-1]:
            res.append(node.val)
            node.left, node.right = node.right, node.left

        return self.dfs(node.left, voyage, res) and self.dfs(node.right, voyage, res)


# Solution 2: iterative
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        res = []
        voyage = voyage[::-1]
        stk = [root]

        while stk:
            node = stk.pop()

            if not node:
                continue

            if node.val != voyage.pop():
                return [-1]

            if node.left and node.left.val != voyage[-1]:
                res.append(node.val)
                stk.append(node.left)
                stk.append(node.right)
            else:
                stk.append(node.right)
                stk.append(node.left)

        return res
