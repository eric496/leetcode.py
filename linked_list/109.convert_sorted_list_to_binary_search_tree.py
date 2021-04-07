"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:
Given the sorted linked list: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

"""
Thought process:
    Use two pointers to find the middle node:
    a slow pointer which travels one step forward each time, and a fast pointer which travels two steps.
    Recursively build the tree using the middle node as the root node, 
    Build the left sub tree using the nodes before the middle node, and the right sub tree using the nodes following the middle node.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: two pointers
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return head

        if not head.next:
            return TreeNode(head.val)

        slow = fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # IMPORTANT: Cut and terminate the linked list to avoid loitering
        prev.next = None
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root


# Solution 2: count the length of the linked list
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        
        if not head.next:
            return TreeNode(head.val)
        
        cnt = 0
        cur = head
        
        while cur:
            cur = cur.next
            cnt += 1
            
        prev = cur = head
        
        for _ in range(cnt//2):
            prev = cur
            cur = cur.next
        
        # IMPORTANT: Cut and terminate the linked list to avoid loitering
        prev.next = None
        root = TreeNode(cur.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(cur.next)
        
        return root
