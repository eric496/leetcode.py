"""
Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.
The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.

Example 1:
Input: 
A binary tree as following:
       4
     /   \
    2     6
   / \   / 
  3   1 5   

v = 1
d = 2
Output: 
       4
      / \
     1   1
    /     \
   2       6
  / \     / 
 3   1   5   

Example 2:
Input: 
A binary tree as following:
      4
     /   
    2    
   / \   
  3   1    

v = 1
d = 3
Output: 
      4
     /   
    2
   / \    
  1   1
 /     \  
3       1

Note:
The given d is in range [1, maximum depth of the given tree + 1].
The given binary tree has at least one tree node.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recursive
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
            
        self.dfs(root, v, d, 1)
        
        return root
    
    
    def dfs(self, node: TreeNode, v: int, d: int, cur_d: int) -> None:
        if not node:
            return
        
        if cur_d == d-1:
            left = node.left
            node.left = TreeNode(v)
            node.left.left = left
            
            right = node.right
            node.right = TreeNode(v)
            node.right.right = right
            
            return
        
        self.dfs(node.left, v, d, cur_d+1)
        self.dfs(node.right, v, d, cur_d+1)
        

# Solution 2: iterative
from collections import deque

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
        
        q = deque([root])
        cur_d = 1
        
        while q:
            if cur_d == d-1:
                for _ in range(len(q)):
                    node = q.popleft()
                    
                    left = node.left
                    node.left = TreeNode(v)
                    node.left.left = left
                    
                    right = node.right
                    node.right = TreeNode(v)
                    node.right.right = right
                    
                break
            else:
                cur_d += 1
                
                for _ in range(len(q)):
                    node = q.popleft()
                    
                    if node.left:
                        q.append(node.left)
                        
                    if node.right:
                        q.append(node.right)
        
        return root
        