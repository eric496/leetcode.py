"""
A full binary tree is a binary tree where each node has exactly 0 or 2 children.
Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.
Each node of each tree in the answer must have node.val = 0.
You may return the final list of trees in any order.

Note:
1 <= N <= 20
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.lookup = {}
    
    
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0:
            return []
        
        if N == 1:
            return [TreeNode(0)]
        
        if N in self.lookup:
            return self.lookup[N]
        
        res = []
        
        for i in range(1, N, 2):
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(N-i-1):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    res.append(root)
                    
        self.lookup[N] = res
        
        return res
        