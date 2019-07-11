"""
You need to find the largest value in each row of a binary tree.

Example:
Input: 
          1
         / \
        3   2
       / \   \  
      5   3   9 
Output: [1, 3, 9]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        q = deque([root])
        res = []
        
        while q:
            size = len(q)
            level_max = float('-inf')
            
            for _ in range(size):
                node = q.popleft()
                level_max = max(level_max, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(level_max)
            
        return res
