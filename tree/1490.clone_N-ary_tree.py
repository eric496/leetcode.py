"""
Given a root of an N-ary tree, return a deep copy (clone) of the tree.
Each node in the n-ary tree contains a val (int) and a list (List[Node]) of its children.

class Node {
    public int val;
    public List<Node> children;
}
Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Follow up: Can your solution work for the graph problem?

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,null,3,2,4,null,5,6]

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]

Constraints:
The depth of the n-ary tree is less than or equal to 1000.
The total number of nodes is between [0, 10^4].
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


# Solution 1: BFS
from collections import deque, defaultdict


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        mp = defaultdict(Node) 
        q = deque([root])
        
        while q:
            node = q.popleft()
            mp[node].val = node.val
            
            for child in node.children:
                q.append(child)
                mp[node].children.append(mp[child])
                
        return mp[root]


# Solution 2: DFS
class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        new_root = Node(root.val)
        
        for child in root.children:
            new_root.children.append(self.cloneTree(child))
            
        return new_root
        