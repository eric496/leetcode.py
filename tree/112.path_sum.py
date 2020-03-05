'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recurisve - by adding up node values
class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        if not root:
            return False
        
        return self.dfs(root, 0, target)
    
    
    def dfs(self, node: TreeNode, cur: int, target: int) -> bool:
        if not node:
            return False
        
        cur += node.val
        
        if cur == target and not node.left and not node.right:
            return True
        
        return self.dfs(node.left, cur, target) or self.dfs(node.right, cur, target)


# Solution 1: recursive - by decrementing the target value
class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        if not root:
            return False
        
        if root.val == target and not root.left and not root.right:
            return True
        
        return self.hasPathSum(root.left, target-root.val) or self.hasPathSum(root.right, target-root.val)


# Solution 2: iterative - by adding up node values
class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        if not root:
            return False
        
        stk = [(root, root.val)]      
        
        while stk:
            node, val = stk.pop()
            
            if val == target and not node.left and not node.right:
                return True
            else:
                if node.left:
                    stk.append((node.left, val+node.left.val))
                if node.right:
                    stk.append((node.right, val+node.right.val))
                    
        return False


# Solution 2: iterative - by decrementing the target value
class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        stk = [(root, target)]

        while stk:
            node, value = stk.pop()
            if node:
                if not node.left and not node.right and node.val == value:
                    return True
                else:
                    stk.append((node.left, value-node.val))
                    stk.append((node.right, value-node.val))
        
        return False
