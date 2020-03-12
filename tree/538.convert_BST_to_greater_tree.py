"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:
Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recursive
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        cumsum = [0]
        self.dfs(root, cumsum)
        
        return root
        
        
    def dfs(self, node: TreeNode, cumsum: List[int]) -> None:
        if not node:
            return
        
        self.dfs(node.right, cumsum)
        node.val += cumsum[0]
        cumsum[0] = node.val
        self.dfs(node.left, cumsum)


# Solution 2: iterative
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        stk = []
        cumsum = 0
        cur = root
        
        while stk or cur:
            while cur:
                stk.append(cur)
                cur = cur.right
                
            node = stk.pop()
            node.val += cumsum
            cumsum = node.val
            cur = node.left
                
        return root


# Solution 2: iterative - a variation
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        stk = []
        cumsum = 0
        cur = root
        
        while stk or cur:
            if cur:
                stk.append(cur)
                cur = cur.right
            else:
                cur = stk.pop()
                cur.val += cumsum
                cumsum = cur.val
                cur = cur.left
        
        return root
        