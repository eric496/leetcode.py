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


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        head = Node(0, None, None)
        stk, cur, prev = [], root, head
        
        while stk or cur:
            while cur:
                stk.append(cur)
                cur = cur.left
            cur = stk.pop()
            cur.left = prev
            prev.right = cur
            prev = cur
            cur = cur.right
        
        head.right.left = prev
        prev.right = head.right
        
        return head.right


# Solution 2: divide and conquer
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        left = self.treeToDoublyList(root.left)
        right = self.treeToDoublyList(root.right)
        root.left = root
        root.right = root
        
        return self.buildLink(self.buildLink(left, root), right)
    
    
    def buildLink(self, n1: 'Node', n2: 'Node') -> 'Node':
        if None in (n1, n2):
            return n1 or n2
        
        t1 = n1.left
        t2 = n2.left
        t1.right = n2
        n2.left = t1
        t2.right = n1
        n1.left = t2
        
        return n1
        