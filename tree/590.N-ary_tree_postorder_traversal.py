"""
Given an n-ary tree, return the postorder traversal of its nodes' values.

Note:
Recursive solution is trivial, could you do it iteratively?
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


# Solution 1: recursive
class Solution:
    def postorder(self, root: "Node") -> List[int]:
        res = []
        self.dfs(root, res)

        return res

    def dfs(self, node: "Node", res: List[int]) -> None:
        if not node:
            return

        for child in node.children:
            self.dfs(child, res)

        res.append(node.val)


# Solution 2: iterative
class Solution:
    def postorder(self, root: "Node") -> List[int]:
        if not root:
            return []

        stk, res = [root], []

        while stk:
            top = stk.pop()
            res.append(top.val)

            for child in top.children:
                stk.append(child)

        return res[::-1]
