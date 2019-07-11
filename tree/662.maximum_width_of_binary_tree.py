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


from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        q = deque([(root, 1)])
        level_width = max_width = 0
        
        while q:
            size = len(q)
            level_width = q[-1][1] - q[0][1] + 1
            max_width = max(max_width, level_width)
            
            for _ in range(size):
                node, pos = q.popleft()
                if node.left:
                    q.append((node.left, 2*pos))
                if node.right:
                    q.append((node.right, 2*pos+1))
            
        return max_width