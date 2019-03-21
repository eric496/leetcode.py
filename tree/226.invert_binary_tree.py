'''
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive solution
class Solution:
    def invertTree(self, root:TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root

# Iterative solution
class Solution:
    def invertTree(self, root:TreeNode) -> TreeNode:
        if not root:
            return root

        stk = []
        stk.append(root)

        while stk:
            node = stk.pop()
            node.left, node.right = node.right, node.left

            if node.left:
                stk.append(node.left)
            if node.right:
                stk.append(node.right)


        return root
