'''
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recursive
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.dfs(root, 0)
        
        
    def dfs(self, node: TreeNode, cur_h: int) -> int:
        if not node:
            return cur_h
        
        return max(self.dfs(node.left, cur_h+1), self.dfs(node.right, cur_h+1))


# Solution 1: more concise
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# Solution 2: iterative - level order traversal
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        depth, q = 0, [root]

        while q:
            depth += 1
            level = []

            for _ in range(len(q)):
                node = q.pop()

                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
        
            q = level
            
        return depth
