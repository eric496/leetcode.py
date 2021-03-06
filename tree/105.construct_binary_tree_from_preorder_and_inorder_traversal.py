"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
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


# Recursive
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.build(0, 0, len(inorder) - 1, preorder, inorder)

    def build(
        self,
        prestart: int,
        instart: int,
        inend: int,
        preorder: List[int],
        inorder: List[int],
    ) -> TreeNode:
        if prestart > len(preorder) - 1 or instart > inend:
            return None

        idx = inorder.index(preorder[prestart])
        root = TreeNode(preorder[prestart])
        root.left = self.build(prestart + 1, instart, idx - 1, preorder, inorder)
        root.right = self.build(
            prestart + idx - instart + 1, idx + 1, inend, preorder, inorder
        )

        return root


# Improved
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        mp = {n: i for i, n in enumerate(inorder)}

        return self.build_tree(0, 0, len(inorder) - 1, preorder, inorder, mp)

    def build_tree(
        self,
        prestart: int,
        instart: int,
        inend: int,
        preorder: List[int],
        inorder: List[int],
        mp: dict,
    ) -> TreeNode:
        if prestart >= len(preorder) or instart > inend:
            return None

        root = TreeNode(preorder[prestart])
        idx = mp[preorder[prestart]]
        root.left = self.build_tree(
            prestart + 1, instart, idx - 1, preorder, inorder, mp
        )
        root.right = self.build_tree(
            prestart + idx - instart + 1, idx + 1, inend, preorder, inorder, mp
        )

        return root
