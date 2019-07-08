"""
Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \ 
1        7   9
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9  

Note:
The number of nodes in the given tree will be between 1 and 100.
Each node will have a unique integer value from 0 to 1000.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: Recursion
class Solution:
    prev, head = None, None
    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        self.increasingBST(root.left)
        
        if self.prev:
            root.left = None
            self.prev.right = root
            
        if not self.head:
            self.head = root
        
        self.prev = root
        self.increasingBST(root.right)
        
        return self.head


# Solution 2: Iterative
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        new = head = TreeNode(0)
        stk = []

        while stk or root:
            while root:
                stk.append(root)
                root = root.left

            root = stk.pop()
            new.right = root
            new = new.right
            root = root.right
            new.left = None

        return head.right
        