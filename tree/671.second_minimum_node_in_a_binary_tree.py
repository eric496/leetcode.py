"""
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.
Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.
If no such second minimum value exists, output -1 instead.

Example 1:
Input: 
    2
   / \
  2   5
     / \
    5   7
Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.

Example 2:
Input: 
    2
   / \
  2   2
Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: BFS
from collections import deque

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        vals = set()
        q = deque([root])
        
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                vals.add(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
        vals.remove(min(vals))
        
        return min(vals) if vals else -1


# Solution 2: DFS
class Solution:
    res = float('inf')
    
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        
        self.dfs(root, root.val)
        
        return self.res if self.res != float('inf') else -1
        
    
    def dfs(self, node: TreeNode, min_val: int) -> None:
        if min_val < node.val < self.res:
            self.res = node.val
        
        if node.left and node.left.val < self.res:
            self.dfs(node.left, min_val)
        
        if node.right and node.right.val < self.res:
            self.dfs(node.right, min_val)
            