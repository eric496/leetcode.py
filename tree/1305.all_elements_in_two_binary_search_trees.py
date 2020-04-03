"""
Given two binary search trees root1 and root2.
Return a list containing all the integers from both trees sorted in ascending order.

Example 1:
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]

Example 2:
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]

Example 3:
Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]

Example 4:
Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]

Example 5:
Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]

Constraints:
Each tree has at most 5000 nodes.
Each node's value is between [-10^5, 10^5].
Accepted
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        arr1, arr2 = [], []
        self.dfs(root1, arr1)
        self.dfs(root2, arr2)

        return self.merge(arr1, arr2)

    def dfs(self, root: TreeNode, res: List[int]) -> None:
        if not root:
            return

        self.dfs(root.left, res)
        res.append(root.val)
        self.dfs(root.right, res)

    def merge(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if None in (arr1, arr2):
            return arr1 or arr2

        res = [0] * (len(arr1) + len(arr2))
        i = j = k = 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                res[k] = arr1[i]
                i += 1
            else:
                res[k] = arr2[j]
                j += 1

            k += 1

        while i < len(arr1):
            res[k] = arr1[i]
            i += 1
            k += 1

        while j < len(arr2):
            res[k] = arr2[j]
            j += 1
            k += 1

        return res
