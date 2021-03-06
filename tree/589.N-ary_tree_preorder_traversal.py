"""
Given an n-ary tree, return the preorder traversal of its nodes' values.

Note:
Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


# Solution 1: recursive
class Solution:
    def preorder(self, root: "Node") -> List[int]:
        res = []
        self.dfs(root, res)

        return res

    def dfs(self, node: "Node", res: List[int]) -> None:
        if not node:
            return

        res.append(node.val)

        for child in node.children:
            self.dfs(child, res)


# Solution 2: iterative
class Solution:
    def preorder(self, root: "Node") -> List[int]:
        if not root:
            return []

        stk, res = [root], []

        while stk:
            node = stk.pop()
            res.append(node.val)

            for child in node.children[::-1]:
                stk.append(child)

        return res
