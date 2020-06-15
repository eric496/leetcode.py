"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:
Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2

Example 2:
Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""


# Solution 1: union find with path compression
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        roots = list(range(n))

        for v, w in edges:
            r1 = self.find(roots, v)
            r2 = self.find(roots, w)

            if r1 != r2:
                roots[r2] = r1
                n -= 1

        return n

    def find(self, roots: List[int], key: int) -> int:
        while roots[key] != key:
            roots[key] = roots[roots[key]]
            key = roots[key]

        return key
