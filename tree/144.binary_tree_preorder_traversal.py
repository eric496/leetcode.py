"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1: DFS
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root: TreeNode, res: List[int]) -> None:
        if not root:
            return

        res.append(root.val)
        self.dfs(root.left, res)
        self.dfs(root.right, res)

# Solution 2: Stack
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stk, res = [root], []

        while stk:
            node = stk.pop()
            res.append(node.val)

            if node.right:
                stk.append(node.right)
            if node.left:
                stk.append(node.left)

        return res

# Solution 3: Stack
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stk, res, node = [], [], root
        
        while stk or node:
            if node:
                stk.append(node)
                res.append(node.val)
                node = node.left
            else:
                node = stk.pop()
                node = node.right
        
        return res

