"""
Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example, 
Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:
         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:
         5
       /   \
      2     7
     / \   
    1   3
         \
          4
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: DFS - always insert the node at the very bottom
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
            
        return root


# Solution 2: Iterative
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        walk = root
        
        while 1:
            if val > walk.val:
                if walk.right:
                    walk = walk.right
                else:
                    walk.right = TreeNode(val)
                    break
            else:
                if walk.left:
                    walk = walk.left
                else:
                    walk.left = TreeNode(val)
                    break
                    
        return root
        