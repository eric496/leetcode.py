"""
A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.
Write a data structure CBTInserter that is initialized with a complete binary tree and supports the following operations:
CBTInserter(TreeNode root) initializes the data structure on a given tree with head node root;
CBTInserter.insert(int v) will insert a TreeNode into the tree with value node.val = v so that the tree remains complete, and returns the value of the parent of the inserted TreeNode;
CBTInserter.get_root() will return the head node of the tree.

Example 1:
Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
Output: [null,1,[1,2]]

Example 2:
Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
Output: [null,3,4,[1,2,3,4,5,6,7,8]]

Note:
The initial given tree is complete and contains between 1 and 1000 nodes.
CBTInserter.insert is called at most 10000 times per test case.
Every value of a given or inserted node is between 0 and 5000.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution: use an array to represent complete binary tree (similar to heap data structure)
from collections import deque


class CBTInserter:
    def __init__(self, root: TreeNode):
        self.res = self.traverse(root, [None])

    def insert(self, v: int) -> int:
        node = TreeNode(v)
        self.res.append(node)
        idx = len(self.res) - 1

        if idx % 2 == 0:
            self.res[idx // 2].left = node
        else:
            self.res[idx // 2].right = node

        return self.res[idx // 2].val

    def get_root(self) -> TreeNode:
        return self.res[1]

    def traverse(self, root: TreeNode, res: List[int]) -> None:
        if not root:
            return res

        q = deque([root])

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                res.append(node)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return res
