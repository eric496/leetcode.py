"""
A binary tree is univalued if every node in the tree has the same value.
Return true if and only if the given tree is univalued.

Example 1:
Input: [1,1,1,1,1,null,1]
Output: true

Example 2:
Input: [2,2,2,5,2]
Output: false

Note:
The number of nodes in the given tree will be in the range [1, 100].
Each node's value will be an integer in the range [0, 99].
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return False

        q, unival = deque([root]), root.val

        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node.val != unival:
                    return False
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return True

