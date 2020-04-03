"""
Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.
The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.  Each node has labels in the set {0, 1, ..., edges.length}.

Example 1:
Input: edges = [[0,1],[0,2]]
Output: 2
Explanation: 
A longest path of the tree is the path 1 - 0 - 2.

Example 2:
Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
Output: 4
Explanation: 
A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.

Constraints:
0 <= edges.length < 10^4
edges[i][0] != edges[i][1]
0 <= edges[i][j] <= edges.length
The given edges form an undirected tree.
"""


"""
Thought process:
    Two rounds of BFS:
        1. First round: start from a random node and traverse the graph to find the furthest node from it.
        2. Second round: start from this furthest node and find the furthest node from it. This path is the diameter.
"""


# Solution: two rounds of BFS
from collections import deque


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0

        adjacent = {}

        for u, v in edges:
            if u in adjacent:
                adjacent[u].add(v)
            else:
                adjacent[u] = {v}

            if v in adjacent:
                adjacent[v].add(u)
            else:
                adjacent[v] = {u}

        node1, _ = self.bfs(edges[0][0], adjacent)
        _, diameter = self.bfs(node1, adjacent)

        return diameter

    def bfs(self, node: int, adjacent: dict) -> tuple:
        dist = 0
        last_node = node
        visited = set()
        q = deque([node])

        while q:
            dist += 1

            for _ in range(len(q)):
                node = q.popleft()

                if node in adjacent:
                    for adj in adjacent[node]:
                        if adj not in visited:
                            visited.add(adj)
                            q.append(adj)
                            last_node = adj

        # dist is the number of nodes along the longest path
        # dist-1 to get the number of edges
        return last_node, dist - 1
