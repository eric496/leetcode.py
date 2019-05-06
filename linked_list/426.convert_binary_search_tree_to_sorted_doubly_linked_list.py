"""
Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.
We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.
Specifically, we want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. We should return the pointer to the first element of the linked list.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        dummy = Node(0, None, None)
        stk, node, prev = [], root, dummy
        
        while stk or node:
            while node:
                stk.append(node)
                node = node.left
            
            node = stk.pop()
            node.left = prev
            prev.right = node
            prev = node
            node = node.right
        
        dummy.right.left = prev
        prev.right = dummy.right
        
        return dummy.right
