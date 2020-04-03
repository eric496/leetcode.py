"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Example:
Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}

Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B.

Note:
You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
"""


# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# Solution 1: recursive
class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return None

        if not root.left and not root.right:
            return root

        if root and root.left and root.right:
            root.left.next = root.right

            if root.next:
                root.right.next = root.next.left

            self.connect(root.left)
            self.connect(root.right)

        return root


# Solution 2: iterative - level order traversal with O(n) space
from collections import deque


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return root

        q = deque([root])

        while q:
            size = len(q)

            for i in range(size):
                node = q.popleft()

                if i == size - 1:
                    node.next = None
                else:
                    node.next = q[0]

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return root


# Solution 2: iterative - level order traversal with O(1) space
class Solution:
    def connect(self, root: "Node") -> "Node":
        level_start = root

        while level_start:
            level_walk = level_start

            while level_walk:
                if level_walk.left:
                    level_walk.left.next = level_walk.right

                if level_walk.right and level_walk.next:
                    level_walk.right.next = level_walk.next.left

                level_walk = level_walk.next

            level_start = level_start.left

        return root
