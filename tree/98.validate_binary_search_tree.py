"""
Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input:
    2s
   / \
  1   3
Output: true

Example 2:
    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: inorder traversal
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = []
        self.inorder(root, res)
        
        for i in range(1, len(res)):
            if res[i] <= res[i-1]:
                return False
        
        return True
        
    
    def inorder(self, root: TreeNode, res: List[int]) -> None:
        if not root:
            return
        
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)


# Solution 1: inorder traversal improved - no need to keep all nodes but only the previous node
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.inorder(root, [float('-inf')])
        
    
    def inorder(self, root: TreeNode, prev: List[int]) -> bool:
        if not root:
            return True
        
        if not self.inorder(root.left, prev):
            return False
        
        if prev[0] >= root.val:
            return False
        
        prev[0] = root.val
        
        if not self.inorder(root.right, prev):
            return False
        
        return True


# Solution 2: recursive
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate(root, float('-inf'), float('inf'))


    def validate(self, root: TreeNode, lower: float, upper: float) -> bool:
        if not root:
            return True
            
        if root.val <= lower or root.val >= upper:
            return False

        return self.validate(root.left, lower, root.val) and self.validate(root.right, root.val, upper)


# Solution 2: iterative
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stk = []
        prev = None
        
        while root or stk:
            while root:
                stk.append(root)
                root = root.left
                
            node = stk.pop()

            if prev and node.val <= prev.val:
                return False
            
            prev = node
            root = node.right
            
        return True
        