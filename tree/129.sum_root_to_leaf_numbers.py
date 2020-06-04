"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:
Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recursive
from typing import List


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = []
        self.dfs(root, 0, res)

        return sum(res)

    def dfs(self, node: TreeNode, cursum: int, res: List[int]) -> None:
        if not node:
            return

        # Reach at a leaf node
        if not node.left and not node.right:
            res.append(cursum * 10 + node.val)

        self.dfs(node.left, cursum * 10 + node.val, res)
        self.dfs(node.right, cursum * 10 + node.val, res)


# Solution 2: recursive
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = [0]
        self.dfs(root, [], res)
        
        return res[0]
        
    def dfs(self, root: TreeNode, path: List[str], res: List[int]) -> None:
        if not root:
            return
        
        if not root.left and not root.right:
            path.append(str(root.val))
            res[0] += int("".join(path))
            return
        
        self.dfs(root.left, path + [str(root.val)], res)
        self.dfs(root.right, path + [str(root.val)], res)


# Solution 3: iterative
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        stk, res = [(root, root.val)], 0

        while stk:
            node, val = stk.pop()

            if node:
                if not node.left and not node.right:
                    res += val

                if node.left:
                    stk.append((node.left, val * 10 + node.left.val))

                if node.right:
                    stk.append((node.right, val * 10 + node.right.val))

        return res
