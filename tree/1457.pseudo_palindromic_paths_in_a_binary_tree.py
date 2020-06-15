"""
Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.
Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

Example 1:
Input: root = [2,3,1,3,1,null,1]
Output: 2 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 2:
Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 3:
Input: root = [9]
Output: 1

Constraints:
The given binary tree will have between 1 and 10^5 nodes.
Node values are digits from 1 to 9.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1
class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        paths = []
        self.dfs(root, 0, paths)
        res = 0

        for path in paths:
            if self.is_palindromic(path):
                res += 1

        return res

    def dfs(self, root: TreeNode, path: int, paths: List[int]) -> None:
        if not root:
            return

        if not root.left and not root.right:
            path = path * 10 + root.val
            paths.append(path)
            return

        self.dfs(root.left, path * 10 + root.val, paths)
        self.dfs(root.right, path * 10 + root.val, paths)

    def is_palindromic(self, path: int) -> bool:
        cnt = [0] * 10

        while path:
            cnt[path % 10] += 1
            path //= 10

        odd = 0

        for n in cnt:
            odd += 1 if n & 1 else 0

        return odd <= 1
