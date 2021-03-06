"""
Given a binary tree, find the length of the longest consecutive sequence path.
The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

Example 1:
Input:
   1
    \
     3
    / \
   2   4
        \
         5
Output: 3
Explanation: Longest consecutive sequence path is 3-4-5, so return 3.

Example 2:
Input:
   2
    \
     3
    / 
   2    
  / 
 1
Output: 2 
Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recursive
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = [0]
        self.dfs(root, 0, root.val, res)

        return res[0]

    def dfs(self, node: TreeNode, cur: int, target: int, res: List[int]) -> None:
        if not node:
            return

        if node.val == target:
            cur += 1
        else:
            cur = 1

        res[0] = max(res[0], cur)

        self.dfs(node.left, cur, node.val + 1, res)
        self.dfs(node.right, cur, node.val + 1, res)


# Solution 2: iterative
from collections import deque


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0

        q = deque([(root, 1)])
        res = 1

        while q:
            node, cur = q.popleft()
            res = max(res, cur)

            if node.left:
                if node.left.val == node.val + 1:
                    q.append([node.left, cur + 1])
                else:
                    q.append([node.left, 1])

            if node.right:
                if node.right.val == node.val + 1:
                    q.append([node.right, cur + 1])
                else:
                    q.append([node.right, 1])

        return res
