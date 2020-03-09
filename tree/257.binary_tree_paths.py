'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recursive
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
        res = []
        self.dfs(root, [], res)
        res = ['->'.join(x) for x in res]
        
        return res
        
        
    def dfs(self, node: TreeNode, cur: List[int], res: List[List[int]]) -> None:
        if not node:
            return
        
        # A leaf is found, append path to the answer list
        if not node.left and not node.right:
            cur.append(str(node.val))
            res.append(cur)
            return
        
        self.dfs(node.left, cur+[str(node.val)], res)
        self.dfs(node.right, cur+[str(node.val)], res)


# Solution 2: iterative 
class Solution:
    def binaryTreePaths(self, root:TreeNode) -> list:
        if not root:
            return []

        res, stk = [], [(root, str(root.val))]
        
        while stk:
            node, path = stk.pop()
            
            if not node.left and not node.right:
                res.append(path)
            
            if node.left:
                stk.append((node.left, path+'->'+str(node.left.val)))
            
            if node.right:
                stk.append((node.right, path+'->'+str(node.right.val)))
        
        return res
        