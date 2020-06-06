"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
   
Note:
Bonus points if you could solve it both recursively and iteratively.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recursive
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.dfs(root.left, root.right)

    def dfs(self, left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True

        if None in (left, right):
            return False

        if left.val != right.val:
            return False

        return self.dfs(left.left, right.right) and self.dfs(left.right, right.left)


# Solution 2: iterative
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        stk = [(root.left, root.right)]

        while stk:
            n1, n2 = stk.pop()

            if not n1 and not n2:
                continue
            
            if None in (n1, n2):
                return False
            
            if n1.val != n2.val:
                return False

            stk.append((n1.left, n2.right))
            stk.append((n1.right, n2.left))

        return True


# Soltuion 3: iterative - level order traversal
from collections import deque


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        q = deque([root])
        
        while q:
            size = len(q)
            level = []
            
            for _ in range(size):
                node = q.popleft()
                
                if node:        
                    q.append(node.left)
                    q.append(node.right)
                    level.append(node.val)
                else:
                    level.append(None)
                    
            if level != level[::-1]:
                return False
            
            
        return True
