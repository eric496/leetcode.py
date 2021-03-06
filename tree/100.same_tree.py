"""
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]
Output: true

Example 2:
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]
Output: false

Example 3:
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]
Output: false
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recursive solution
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True

        if None in (p, q):
            return False

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# Solution 2: iterative solution
from collections import deque

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        res = deque([(p, q)])

        while res:
            n1, n2 = res.popleft()

            if not n1 and not n2:
                continue

            if None in (n1, n2):
                return False

            if n1.val != n2.val:
                return False

            res.append((n1.left, n2.left))
            res.append((n1.right, n2.right))

        return True
