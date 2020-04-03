"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 
You may serialize the following tree:
    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]"

Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: recursive
from collections import deque


class Codec:
    def serialize(self, root: TreeNode) -> str:
        res = []
        self.build_string(root, res)
        return "".join(res)

    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None

        q = deque([x for x in data.split("#")])
        return self.build_tree(q)

    def build_string(self, root: TreeNode, res: List[str]) -> None:
        if root:
            res.append(str(root.val))
            res.append("#")
            self.build_string(root.left, res)
            self.build_string(root.right, res)
        else:
            res.append("X")
            res.append("#")

    def build_tree(self, q) -> TreeNode:
        if q:
            val = q.popleft()
            if val == "X":
                return None
            else:
                root = TreeNode(int(val))
                root.left = self.build_tree(q)
                root.right = self.build_tree(q)
                return root


# Solution 2: iterative
