"""
Return the root node of a binary search tree that matches the given preorder traversal.
(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

Example 1:
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Note: 
1 <= preorder.length <= 100
The values of preorder are distinct.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recursive
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return self.dfs(preorder, float("-inf"), float("inf"), [0])

    def dfs(
        self, preorder: List[int], lower: int, upper: int, idx: List[int]
    ) -> TreeNode:
        if (
            idx[0] == len(preorder)
            or preorder[idx[0]] < lower
            or preorder[idx[0]] > upper
        ):
            return None

        node = TreeNode(preorder[idx[0]])
        idx[0] += 1
        node.left = self.dfs(preorder, lower, node.val, idx)
        node.right = self.dfs(preorder, node.val, upper, idx)

        return node


# Solution 2: iterative
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stk = [root]

        for i in range(1, len(preorder)):
            val = preorder[i]
            node = TreeNode(val)

            if val < stk[-1].val:
                stk[-1].left = node
            else:
                while stk and stk[-1].val <= val:
                    prev = stk.pop()

                prev.right = node

            stk.append(node)

        return root
