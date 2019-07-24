"""
Given a binary tree where every node has a unique value, and a target key k, find the value of the nearest leaf node to target k in the tree.
Here, nearest to a leaf means the least number of edges travelled on the binary tree to reach any leaf of the tree. Also, a node is called a leaf if it has no children.
In the following examples, the input tree is represented in flattened form row by row. The actual root tree given will be a TreeNode object.

Example 1:
Input:
root = [1, 3, 2], k = 1
Diagram of binary tree:
          1
         / \
        3   2
Output: 2 (or 3)
Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.

Example 2:
Input:
root = [1], k = 1
Output: 1
Explanation: The nearest leaf node is the root node itself.

Example 3:
Input:
root = [1,2,3,4,null,null,null,5,null,6], k = 2
Diagram of binary tree:
             1
            / \
           2   3
          /
         4
        /
       5
      /
     6
Output: 3
Explanation: The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.

Note:
root represents a binary tree with at least 1 node and at most 1000 nodes.
Every node has a unique node.val in range [1, 1000].
There exists some node in the given binary tree for which node.val == k.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    
    def __init__(self):
        self.graph = {}
        self.leaves = set()
    
    
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        self.dfs(root)
        q = [k]
        
        while q:
            one_step_away = []
            for val in q:
                if val in self.leaves:
                    return val
                one_step_away += self.graph.pop(val, [])
            q = one_step_away
        
        return -1
        
        
    def dfs(self, node: TreeNode) -> None:
        if not node:
            return
        
        if node.left is None and node.right is None:
            self.leaves.add(node.val)
            return
        
        if node.left:
            if node.val in self.graph:
                self.graph[node.val].append(node.left.val)
            else:
                self.graph[node.val] = [node.left.val]
                
            if node.left.val in self.graph:
                self.graph[node.left.val].append(node.val)
            else:
                self.graph[node.left.val] = [node.val]

            self.dfs(node.left)
            
        if node.right:
            if node.val in self.graph:
                self.graph[node.val].append(node.right.val)
            else:
                self.graph[node.val] = [node.right.val]
                
            if node.right.val in self.graph:
                self.graph[node.right.val].append(node.val)
            else:
                self.graph[node.right.val] = [node.val]
                
            self.dfs(node.right)
        