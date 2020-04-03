"""
Given two binary search trees, return True if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.

Example 1:
Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.

Example 2:
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
Output: false

Constraints:
Each tree has at most 5000 nodes.
-10^9 <= target, node.val <= 10^9
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        if not root1 or not root2:
            return False

        stk1, stk2 = [], []
        node1, node2 = TreeNode(None), TreeNode(None)

        while 1:
            while root1:
                stk1.append(root1)
                root1 = root1.left

            while root2:
                stk2.append(root2)
                root2 = root2.right

            if not stk1 or not stk2:
                break

            node1, node2 = stk1[-1], stk2[-1]

            if node1.val + node2.val == target:
                return True
            elif node1.val + node2.val < target:
                stk1.pop()
                root1 = node1.right
            else:
                stk2.pop()
                root2 = node2.left

        return False
