"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

Note:
The range of node's value is in the range of 32-bit signed integer.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recurisve
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:       
        cnt = []
        self.dfs(root, 0, cnt)
        
        return [level_sum/n for level_sum, n in cnt]
        
        
    def dfs(self, node: TreeNode, depth: int, cnt: List[List[int]]) -> None:
        if not node:
            return
        
        if depth == len(cnt):
            cnt.append([0, 0])
        
        cnt[depth][0] += node.val
        cnt[depth][1] += 1
        self.dfs(node.left, depth+1, cnt)
        self.dfs(node.right, depth+1, cnt)


# Solution 2: iterative - level order traversal
from collections import deque

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []

        q, res = deque([root]), []

        while q:
            size, level_sum = len(q), 0
            
            for _ in range(size):
                node = q.popleft()
                level_sum += node.val
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)

            res.append(level_sum/size)

        return res


# Solution 2: iterative - order doesn't matter, so no need to use queue
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        
        res, stk = [], [root]
        
        while stk:
            size = len(stk)
            level = []
            level_sum = 0
            
            for _ in range(size):
                node = stk.pop()
                level_sum += node.val
                
                if node.left:
                    level.append(node.left)
                
                if node.right:
                    level.append(node.right)
                    
            stk = level
            res.append(level_sum/size)
            
        return res


# Solution 2: recursive
 