"""
You are given a binary tree in which each node contains an integer value.
Find the number of paths that sum to a given value.
The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1
Return 3. The paths that sum to 8 are:
1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Prefix sum using a map
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        if not root:
            return 0

        presum = {0: 1}

        return self.backtrack(root, 0, target, presum)

    def backtrack(self, node: TreeNode, cursum: int, target: int, presum: dict) -> int:
        if not node:
            return 0

        cursum += node.val
        res = presum.get(cursum - target, 0)
        presum[cursum] = presum.get(cursum, 0) + 1
        res += self.backtrack(node.left, cursum, target, presum) + self.backtrack(
            node.right, cursum, target, presum
        )
        # backtrack
        presum[cursum] -= 1

        return res
