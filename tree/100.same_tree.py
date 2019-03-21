'''
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive solution 
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q

# iterative solution
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        queue = [(p, q)]
        while queue:
            n1, n2 = queue.pop(0)
            if not n1 and not n2:
                continue
            elif None in [n1, n2]:
                return False
            else:
                if n1.val != n2.val:
                    return False
                queue.append((n1.left, n2.left))
                queue.append((n1.right, n2.right))
        return True
