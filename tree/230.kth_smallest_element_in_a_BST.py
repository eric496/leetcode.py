"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1: inorder traversal
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stk, cnt = [], 0
        node = root

        while stk or node:
            if node:
                stk.append(node)
                node = node.left
            else:
                node = stk.pop()
                cnt += 1
                if cnt == k:
                    return node.val
                node = node.right

        return -1
