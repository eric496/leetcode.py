"""
We are given a binary tree (with root node root), a target node, and an integer value K.
Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
Output: [7,4,1]
Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.
Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 
Note:
The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

from collections import defaultdict

class Solution:
    
    def __init__(self):
        self.graph = defaultdict(set)
        self.visited = set()
        
    
    def distanceK(self, root, target, K):
        self.dfs(root, target.val)
        res = [target.val]
        
        for _ in range(K):
            size, level = len(res), []
            
            for _ in range(size):
                cur = res.pop()
                if cur not in self.visited:
                    level += self.graph.get(cur, [])
                    self.visited.add(cur)
            
            res = level
            
        return [val for val in res if val not in self.visited]
            
    
    def dfs(self, root: TreeNode, target: int) -> None:
        if not root:
            return
        
        if root.left:
            self.graph[root.val].add(root.left.val)
            self.graph[root.left.val].add(root.val)
            self.dfs(root.left, target)
            
        if root.right:
            self.graph[root.val].add(root.right.val)
            self.graph[root.right.val].add(root.val)
            self.dfs(root.right, target)