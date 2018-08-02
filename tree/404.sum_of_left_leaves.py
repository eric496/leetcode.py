'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# first thought
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        queue = [root]
        result = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.pop(0)
                result += node.left.val if node and node.left and (not node.left.left) and (not node.left.right) else 0
                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)
        return result

# optimize a little bit
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        queue = [root]
        result = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.pop(0)
                if node:
                    if node.left:
                        result += node.left.val if (not node.left.left) and (not node.left.right) else 0
                        queue.append(node.left) 
                    if node.right:
                        queue.append(node.right)
        return result