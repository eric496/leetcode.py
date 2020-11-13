"""
Given a binary tree
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Example:
Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":null,"next":null,"right":{"$id":"6","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}
Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":null,"right":null,"val":7},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"6","left":null,"next":null,"right":{"$ref":"5"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"6"},"val":1}
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B.

Follow up:
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


# Level order traversal
from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
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


# Recursive
class Solution:
    def connect(self, root: "Node") -> "Node":
        self.dfs(root)
        return root

    def dfs(self, root: "Node") -> None:
        if not root:
            return

        if not root.left and not root.right:
            return

        if root.left:
            if root.right:
                root.left.next = root.right
            else:
                node = root.next
                while node:
                    if node.left:
                        root.left.next = node.left
                        break
                    elif node.right:
                        root.left.next = node.right
                        break
                    else:
                        node = node.next

        if root.right:
            node = root.next
            while node:
                if node.left:
                    root.right.next = node.left
                    break
                elif node.right:
                    root.right.next = node.right
                    break
                else:
                    node = node.next

        self.dfs(root.right)
        self.dfs(root.left)
