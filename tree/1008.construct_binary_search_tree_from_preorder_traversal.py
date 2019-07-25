"""
Return the root node of a binary search tree that matches the given preorder traversal.
(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

Example 1:
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Note: 
1 <= preorder.length <= 100
The values of preorder are distinct.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stk = [root]
        
        for val in preorder[1:]:
            if val < stk[-1].val:
                stk[-1].left = TreeNode(val)
                stk.append(stk[-1].left)
            else:
                while stk and stk[-1].val <= val:
                    prev = stk.pop()
                
                prev.right = TreeNode(val)
                stk.append(prev.right)
            
        return root
        