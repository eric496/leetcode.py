"""
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Note:
Both of the given trees will have between 1 and 100 nodes.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: inorder traversal
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaves1, leaves2 = [], []
        self.getLeaves(root1, leaves1)
        self.getLeaves(root2, leaves2)

        return leaves1 == leaves2

    def getLeaves(self, root: TreeNode, leaves: List[int]) -> None:
        if not root:
            return

        if not root.left and not root.right:
            leaves.append(root.val)

        self.getLeaves(root.left, leaves)
        self.getLeaves(root.right, leaves)


# Solution 2: more concise
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.dfs(root1) == self.dfs(root2)

    def dfs(self, node: TreeNode) -> List[int]:
        if not node:
            return []

        if not node.left and not node.right:
            return [node.val]

        return self.dfs(node.left) + self.dfs(node.right)
