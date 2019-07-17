"""
Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.

Example 1:
Input: [1,3,null,null,2]
   1
  /
 3
  \
   2
Output: [3,1,null,null,2]
   3
  /
 1
  \
   2

Example 2:
Input: [3,1,4,null,null,2]
  3
 / \
1   4
   /
  2
Output: [2,1,4,null,null,3]
  2
 / \
1   4
   /
  3

Follow up:
A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
"""

"""
Thought process:
   In-order traversal
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    first = second = None
    prev = TreeNode(float('-inf'))
    
    def recoverTree(self, root: TreeNode) -> None:
        self.dfs(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        
        
    def dfs(self, root: TreeNode) -> None:
        if not root:
            return
        
        self.dfs(root.left)
        
        if not self.first and self.prev.val >= root.val:
            self.first = self.prev
            
        if self.first and self.prev.val >= root.val:
            self.second = root
            
        self.prev = root
        
        self.dfs(root.right)


# Follow up: Morris traversal
