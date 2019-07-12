"""
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.

Example:
Input: [10,5,15,1,8,null,7]
   10 
   / \ 
  5  15 
 / \   \ 
1   8   7
Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one.
             The return value is the subtree's size, which is 3.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        res = self.largestBST(root)
        return res[2]
    
        
    def largestBST(self, node: TreeNode) -> List[int]:
        if not node:
            return [float('inf'), float('-inf'), 0]
        
        left = self.largestBST(node.left)
        right = self.largestBST(node.right)
        
        if node.val > left[1] and node.val < right[0]:
            return [min(node.val, left[0]), max(node.val, right[1]), left[2]+right[2]+1]
        else:
            return [float('-inf'), float('inf'), max(left[2], right[2])]
            