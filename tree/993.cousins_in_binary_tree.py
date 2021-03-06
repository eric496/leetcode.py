"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.

Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

Note:
The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution: level order traversal
from collections import deque


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False

        q = deque([root])

        while q:
            found_x = found_y = False

            for _ in range(len(q)):
                node = q.popleft()

                if node.val == x:
                    found_x = True
                elif node.val == y:
                    found_y = True

                if node.left and node.right:
                    if node.left.val == x and node.right.val == y:
                        return False

                    if node.left.val == y and node.right.val == x:
                        return False

                    # Can be more concise like the following
                    # if {node.left.val, node.right.val} == {x, y}:
                    #     return False

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            if found_x and found_y:
                return True
            elif found_x != found_y:
                return False

        return False
