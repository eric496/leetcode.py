"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1: DFS
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)
        right = root.right

        while root.left:
            root.right = root.left
            root.left = None

            while root.right:
                root = root.right

            root.right = right

# Solution 2: Iterative
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stk, node = [], root

        while stk or node:
            if node.right:
                stk.append(node.right)

            if node.left:
                node.right = node.left
                node.left = None
            elif stk:
                node.right = stk.pop()

            node = node.right

