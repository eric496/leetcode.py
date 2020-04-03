"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following 3-ary tree
as [1 [3[5 6] 2 4]]. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note:
N is in the range of [1, 1000]
Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


from collections import deque


class Codec:
    def serialize(self, root):
        res = []
        self.serialize_dfs(root, res)

        return "".join(res)

    def deserialize(self, data):
        if not data:
            return None

        q = deque([x for x in data.split("#") if x])

        return self.deserialize_dfs(q)

    def serialize_dfs(self, root, res):
        if root:
            res.append(str(root.val) + "#")
            res.append(str(len(root.children)) + "#")

            for child in root.children:
                self.serialize_dfs(child, res)

    def deserialize_dfs(self, q):
        if q:
            val = int(q.popleft())
            num_children = int(q.popleft())
            root = Node(val, [])

            for _ in range(num_children):
                root.children.append(self.deserialize_dfs(q))

            return root
