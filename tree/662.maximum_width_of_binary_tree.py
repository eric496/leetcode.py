"""
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.
The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:
Input: 
           1
         /   \
        3     2
       / \     \  
      5   3     9 
Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

Example 2:
Input: 
          1
         /  
        3    
       / \       
      5   3     
Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).

Example 3:
Input: 
          1
         / \
        3   2 
       /        
      5      
Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).

Example 4:
Input: 
          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).

Note: Answer will in the range of 32-bit signed integer.
"""

"""
Thought process:
    BFS Level order traversal and keep track of the position of the nodes.
    The position of the left child is 2*n and the right child 2*n + 1 where n is the position of its parent node.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recursive
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        start, end = [], []
        self.dfs(root, 0, 1, start, end)
        res = float("-inf")

        for s, e in zip(start, end):
            res = max(res, e - s + 1)

        return res

    def dfs(
        self,
        node: TreeNode,
        depth: int,
        pos: int,
        start: List[List[int]],
        end: List[List[int]],
    ) -> None:
        if not node:
            return

        if depth == len(start):
            start.append(pos)
            end.append(pos)
        else:
            end[depth] = pos

        self.dfs(node.left, depth + 1, 2 * pos, start, end)
        self.dfs(node.right, depth + 1, 2 * pos + 1, start, end)


# Solution 2: iterative
from collections import deque


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        q = deque([(root, 1)])
        width = res = 0

        while q:
            width = q[-1][1] - q[0][1] + 1
            res = max(res, width)

            for _ in range(len(q)):
                node, pos = q.popleft()

                if node.left:
                    q.append([node.left, 2 * pos])

                if node.right:
                    q.append([node.right, 2 * pos + 1])

        return res
