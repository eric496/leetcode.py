"""
Given the root of a binary tree, find the maximum average value of any subtree of that tree.
(A subtree of a tree is any node of that tree plus all its descendants. The average value of a tree is the sum of its values, divided by the number of nodes.)

Example 1:
Input: [5,6,1]
Output: 6.00000
Explanation: 
For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
For the node with value = 6 we have an average of 6 / 1 = 6.
For the node with value = 1 we have an average of 1 / 1 = 1.
So the answer is 6 which is the maximum.

Note:
The number of nodes in the tree is between 1 and 5000.
Each node will have a value between 0 and 100000.
Answers will be accepted as correct if they are within 10^-5 of the correct answer.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution: recursive bottom up
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        res = [float("-inf")]
        self.dfs(root, res)

        return res[0]

    def dfs(self, root: TreeNode, res: List[int]) -> List[int]:
        if not root:
            return [0, 0]

        left_val, left_num = self.dfs(root.left, res)
        right_val, right_num = self.dfs(root.right, res)
        val = root.val + left_val + right_val
        num = left_num + right_num + 1
        res[0] = max(res[0], val / num)

        return [val, num]
