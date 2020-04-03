"""
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1

Note:
The size of the given array will be in the range [1,1000].
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# DFS
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.construct(nums, 0, len(nums) - 1)

    def construct(self, nums: List[int], start: int, end: int) -> TreeNode:
        if start > end:
            return None

        max_idx = nums.index(max(nums[start : end + 1]))
        root = TreeNode(nums[max_idx])
        root.left = self.construct(nums, start, max_idx - 1)
        root.right = self.construct(nums, max_idx + 1, end)

        return root


# Improved
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        lookup = {n: i for i, n in enumerate(nums)}

        return self.construct(nums, 0, len(nums) - 1, lookup)

    def construct(
        self, nums: List[int], start: int, end: int, lookup: dict
    ) -> TreeNode:
        if start > end:
            return None

        max_idx = lookup[max(nums[start : end + 1])]
        root = TreeNode(nums[max_idx])
        root.left = self.construct(nums, start, max_idx - 1, lookup)
        root.right = self.construct(nums, max_idx + 1, end, lookup)

        return root
