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
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1

        root = ListNode(t1.val+t2.val)

        stk1, stk2 = [], []
        stk1.append(t1)
        stk2.append(t2)

        while stk1 and stk2:
            n1, n2 = stk1.pop(0), stk2.pop(0)
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

                stk1.append(n1.left)
                stk1.append(n1.right)
                stk2.append(n2.left)
                stk2.append(n2.right)

        return t1
