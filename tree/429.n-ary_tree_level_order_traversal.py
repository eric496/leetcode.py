"""
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:
We should return its level order traversal:
[
     [1],
     [3,2,4],
     [5,6]
]

Note:
The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
"""


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


# Solution 1: recursive
class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        if not root:
            return []

        res = []
        self.dfs(root, 0, res)

        return res

    def dfs(self, node: "Node", depth: int, res: List[List[int]]) -> None:
        if not node:
            return

        if depth == len(res):
            res.append([])

        res[depth].append(node.val)

        for child in node.children:
            self.dfs(child, depth + 1, res)


# Solution 2: iterative
from collections import deque


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        if not root:
            return []

        q, res = deque([root]), []

        while q:
            level = []

            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.children:
                    for child in node.children:
                        q.append(child)

            res.append(level)

        return res
