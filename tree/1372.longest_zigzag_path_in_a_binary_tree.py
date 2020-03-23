"""
Given a binary tree root, a ZigZag path for a binary tree is defined as follow:
Choose any node in the binary tree and a direction (right or left).
If the current direction is right then move to the right child of the current node otherwise move to the left child.
Change the direction from right to left or right to left.
Repeat the second and third step until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).
Return the longest ZigZag path contained in that tree.

Example 1:
Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

Example 2:
Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).

Example 3:
Input: root = [1]
Output: 0

Constraints:
Each tree has at most 50000 nodes..
Each node's value is between [1, 100].
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if not root:
            return -1
        
        res = [0]
        self.dfs(root.left, 1, 'left', res)
        self.dfs(root.right, 1, 'right', res)
        
        return res[0]
        
    
    def dfs(self, root: TreeNode, path: int, direction: str, res: List[int]) -> None:
        if not root:
            return
        
        res[0] = max(res[0], path)
        
        if direction == 'left':
            self.dfs(root.right, path+1, 'right', res)
            self.dfs(root.left, 1, 'left', res)
        else:
            self.dfs(root.left, path+1, 'left', res)
            self.dfs(root.right, 1, 'right', res)
