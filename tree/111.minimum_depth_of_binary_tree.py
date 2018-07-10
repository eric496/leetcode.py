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

# iterative solution
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        depth = 0
        level = [root] if root else []
        while level:
            depth += 1
            cur_level = []
            for node in level:
                if not node.left and not node.right:
                    return depth
                elif not node.left:
                    cur_level.append(node.right)
                elif not node.right:
                    cur_level.append(node.left)
                else:
                    cur_level.append(node.left)
                    cur_level.append(node.right)
            level = cur_level
        return depth