"""
Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.
We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.
Specifically, we want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. We should return the pointer to the first element of the linked list.
"""


# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


# Solution 1: recursive
class Solution:
    def treeToDoublyList(self, root: "Node") -> "Node":
        if not root:
            return root

        sentinel = prev = Node(None, None, None)
        prev = self.dfs(root, prev)
        prev.right = sentinel.right
        sentinel.right.left = prev

        return sentinel.right


    # Inorder traversal
    def dfs(self, node: "Node", prev: "Node") -> "Node":
        if not node:
            return prev

        prev = self.dfs(node.left, prev)
        prev.right = node
        node.left = prev
        prev = self.dfs(node.right, node)

        return prev


# Solution 2: iterative
class Solution:
    def treeToDoublyList(self, root: "Node") -> "Node":
        if not root:
            return root

        stk = []
        sentinel = prev = Node(None, None, None)
        sentinel.next = cur = root

        while stk or cur:
            while cur:
                stk.append(cur)
                cur = cur.left

            cur = stk.pop()
            cur.left = prev
            prev.right = cur
            prev = cur
            cur = cur.right

        sentinel.right.left = prev
        prev.right = sentinel.right

        return sentinel.right
