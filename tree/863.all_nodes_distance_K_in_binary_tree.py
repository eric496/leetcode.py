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
        

# Solution: DFS to build undirected graph, BFS to traverse nodes
from collections import defaultdict

class Solution:
    
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph = defaultdict(set)
        self.dfs(root, graph)
        q = [target]
        visited = set()
        
        for _ in range(K):
            bfs = []
            
            for _ in range(len(q)):
                cur = q.pop()
                
                if cur not in visited:
                    bfs += graph.get(cur, [])
                    visited.add(cur)
            
            q = bfs
            
        return [node.val for node in q if node not in visited]
            
    
    def dfs(self, node: TreeNode, graph: dict) -> None:
        if not node:
            return
        
        if node.left:
            graph[node].add(node.left)
            graph[node.left].add(node)
            self.dfs(node.left, graph)
            
        if node.right:
            graph[node].add(node.right)
            graph[node.right].add(node)
            self.dfs(node.right, graph)
            