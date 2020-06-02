"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:
Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7


Note: The merging process must start from the root nodes of both trees.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recursive
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if None in (t1, t2):
            return t1 or t2

        root = TreeNode(t1.val + t2.val)
        root.left = self.mergeTrees(t1.left, t2.left)
        root.right = self.mergeTrees(t1.right, t2.right)

        return root


# Solution 2: iterative
from collections import deque


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if None in (t1, t2):
            return t1 or t2

        q1, q2 = deque([t1]), deque([t2])

        while q1 and q2:
            n1, n2 = q1.popleft(), q2.popleft()

            if n1 and n2:
                n1.val += n2.val
                
                if n2.left and not n1.left:
                    n1.left = TreeNode(0)
                # Don't need to check Tree 2, because it already came to a leaf node
                # if n1.left and not n2.left:
                #     n2.left = TreeNode(0)
                if n2.right and not n1.right:
                    n1.right = TreeNode(0)
                # if n1.right and not n2.right:
                #     n2.right = TreeNode(0)

                q1.append(n1.left)
                q1.append(n1.right)
                q2.append(n2.left)
                q2.append(n2.right)

        return t1
