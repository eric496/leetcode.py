"""
Given the root of a binary tree, each node in the tree has a distinct value.
After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
Return the roots of the trees in the remaining forest.  You may return the result in any order.

Example 1:
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]

Constraints:
The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        targets = set(to_delete)
        res = []
        self.dfs(root, False, targets, res)

        return res

    def dfs(
        self, root: TreeNode, parent_exists: bool, targets: set, res: List[TreeNode]
    ) -> TreeNode:
        if not root:
            return None

        if root.val in targets:
            root.left = self.dfs(root.left, False, targets, res)
            root.right = self.dfs(root.right, False, targets, res)
            return None
        else:
            if not parent_exists:
                res.append(root)

            root.left = self.dfs(root.left, True, targets, res)
            root.right = self.dfs(root.right, True, targets, res)
            return root
