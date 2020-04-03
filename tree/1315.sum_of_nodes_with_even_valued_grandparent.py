"""
Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)
If there are no nodes with an even-valued grandparent, return 0.

Example 1:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.

Constraints:
The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recursive
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = [0]
        self.dfs(root, None, None, res)

        return res[0]

    def dfs(
        self, node: TreeNode, parent: TreeNode, grandparent: TreeNode, res: List[int]
    ) -> None:
        if not node:
            return

        if grandparent and grandparent.val % 2 == 0:
            res[0] += node.val

        self.dfs(node.left, node, parent, res)
        self.dfs(node.right, node, parent, res)


# Solution 2: iterative - level order traversal
from collections import deque


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        q = deque([(root, -1)])

        while q:
            for _ in range(len(q)):
                node, parent_val = q.popleft()

                if parent_val % 2 == 0:
                    res += node.left.val if node.left else 0
                    res += node.right.val if node.right else 0

                if node.left:
                    q.append((node.left, node.val))

                if node.right:
                    q.append((node.right, node.val))

        return res
