"""
Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
Return the sum of these numbers.

Example 1:
Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

Note:
The number of nodes in the tree is between 1 and 1000.
node.val is 0 or 1.
The answer will not exceed 2^31 - 1.
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        res = []
        self.dfs(root, '', res)

        return sum(int(n, 2) for n in res)


    def dfs(self, node: TreeNode, cur: str, res: List[str]) -> None:
        if not node.left and not node.right:
            res.append(cur+str(node.val))

        if node.left:
            self.dfs(node.left, cur+str(node.val), res)

        if node.right:
            self.dfs(node.right, cur+str(node.val), res)

