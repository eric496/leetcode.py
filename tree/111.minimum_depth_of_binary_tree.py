'''
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Iterative
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        q, res = [root], 0
        
        while q:
            res += 1
            size = len(q)
            for i in range(size):
                node = q.pop(0)
                if not node.left and not node.right:
                    return res
                elif not node.left:
                    q.append(node.right)
                elif not node.right:
                    q.append(node.left)
                else:
                    q.append(node.left)
                    q.append(node.right)
        return res
        