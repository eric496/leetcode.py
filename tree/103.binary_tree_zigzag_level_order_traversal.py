"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recursive
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.dfs(root, 0, res)
        
        return res
        
    
    def dfs(self, root: TreeNode, depth: int, res: List[deque]) -> None:
        if not root:
            return
        
        if len(res) == depth:
            res.append(deque())
            
        if depth % 2 == 0:
            res[depth].append(root.val)
        else:
            res[depth].appendleft(root.val)
            
        self.dfs(root.left, depth+1, res)
        self.dfs(root.right, depth+1, res)


# Solution 2: iterative using Queue
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        q, res = deque([root]), []
        reverse = False

        while q:
            level = []
            
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            if reverse:
                res.append(level[::-1])
            else:
                res.append(level)
            
            reverse = not reverse

        return res

