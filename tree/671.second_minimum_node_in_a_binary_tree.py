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


# Solution 1: recursive
class Solution:    
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res = [float('inf')]
        self.dfs(root, float('inf'), res)
        
        return res[0] if res[0] != float('inf') else -1
        
    
    def dfs(self, node: TreeNode, min_val: int, res: List[int]) -> None:
        if not node:
            return 
        
        min_val = min(min_val, node.val)
        
        if min_val < node.val < res[0]:
            res[0] = node.val
            # Early stopping
            return 
        else:
            self.dfs(node.left, min_val, res)
            self.dfs(node.right, min_val, res)


# Solution 2: iterative
from collections import deque

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        min_val, second = root.val, float('inf')
        q = deque([root])
        
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                
                if min_val < node.val < second:
                    second = node.val
                                          
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
        return second if second != float('inf') else -1
        