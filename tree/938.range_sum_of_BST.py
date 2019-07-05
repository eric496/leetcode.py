"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
The binary search tree is guaranteed to have unique values.

Example 1:
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23

Note:
The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1: not efficient
class Solution:
    def __init__(self):
        self.res = 0

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root:
            self.res += root.val if L <= root.val <= R else 0
            self.rangeSumBST(root.left, L, R)
            self.rangeSumBST(root.right, L, R)

        return self.res


# Solution 2
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0

        res = 0

        if L <= root.val <= R:
            res += root.val
        if root.val > L:
            res += self.rangeSumBST(root.left, L, R)
        if root.val < R:
            res += self.rangeSumBST(root.right, L, R)

        return res

