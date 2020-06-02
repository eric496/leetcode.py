"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# DFS
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.build(len(postorder) - 1, 0, len(inorder) - 1, inorder, postorder)

    def build(
        self,
        postidx: int,
        instart: int,
        inend: int,
        inorder: List[int],
        postorder: List[int],
    ) -> TreeNode:
        if postidx < 0 or instart > inend:
            return None

        root = TreeNode(postorder[postidx])
        inidx = inorder.index(postorder[postidx])
        root.left = self.build(
            postidx - (inend - inidx) - 1, instart, inidx - 1, inorder, postorder
        )
        root.right = self.build(postidx - 1, inidx + 1, inend, inorder, postorder)

        return root


# Improved

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        mp = {n: i for i, n in enumerate(inorder)}
        
        return self.build(len(postorder) - 1, 0, len(inorder) - 1, postorder, inorder, mp)
    
    def build(self, poststart: int, instart: int, inend: int, postorder: List[int], inorder: List[int], mp: dict) -> TreeNode:
        if poststart < 0 or instart > inend:
            return None
        
        root = TreeNode(postorder[poststart])
        idx = mp[postorder[poststart]]
        root.left = self.build(poststart - (inend - idx) - 1, instart, idx - 1, postorder, inorder, mp)
        root.right = self.build(poststart - 1, idx + 1, inend, postorder, inorder, mp)
        
        return root
