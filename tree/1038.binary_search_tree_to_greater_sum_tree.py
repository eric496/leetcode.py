"""
Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to the sum of the values of the original tree that are greater than or equal to node.val.
As a reminder, a binary search tree is a tree that satisfies these constraints:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
 
Note:
The number of nodes in the tree is between 1 and 100.
Each node will have value between 0 and 100.
The given tree is a binary search tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# DFS
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.dfs(root, 0)
        
        return root
    
        
    def dfs(self, node: TreeNode, val: int) -> None:
        if not node:
            return val
        
        node.val += self.dfs(node.right, val)
        
        return self.dfs(node.left, node.val)


# Iterative: stack
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        stk, cur, sum_ = [], root, 0
        
        while cur or stk:
            while cur:
                stk.append(cur)
                cur = cur.right
            
            cur = stk.pop()
            sum_ += cur.val
            cur.val = sum_
            cur = cur.left
        
        return root
    