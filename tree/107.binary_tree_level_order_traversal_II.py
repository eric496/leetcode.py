'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:

Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list:
        if not root:
            return []

        level, result = [root], [[root.val]]
        while level:
            cur_level = []
            is_there_item_in_next_level = 0
            for item in level:
                if (item.left or item.right) and not is_there_item_in_next_level:
                    result.append([])
                    is_there_item_in_next_level = 1
                if item.left:
                    cur_level.append(item.left)
                    result[-1].append(item.left.val)
                if item.right:
                    cur_level.append(item.right)
                    result[-1].append(item.right.val)
            level = cur_level
        return result[::-1]

# Solution 2
from collections import deque

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        q, res = deque([root]), []
        
        while q:
            level, size = [], len(q)
            for i in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        
        return res[::-1]

# Solution 3: more concise but less readable
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list:
        if not root:
            return []
        q, result = [root], []
        while q:
            result.append([node.val for node in level])
            q = [node for el in q for node in (el.left, el.right) if node]
        return result[::-1]
