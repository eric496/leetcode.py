"""
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.
A critical connection is a connection that, if removed, will make some server unable to reach some other server.
Return all critical connections in the network in any order.

Example 1:
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.

Constraints:
1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.
"""


from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(set)
        
        for u, v in connections:
            graph[u].add(v)
            graph[v].add(u)
            
        visited = set()
        lowest_rank = [0] * n
        res = []
        self.dfs(0, -1, 0, lowest_rank, visited, res, graph)
        
        return res
        
    def dfs(self, rank: int, prev: int, node: int, lowest_rank: List[int], visited: set, res: List[List[int]], graph: dict) -> None:
        visited.add(node)
        lowest_rank[node] = rank
        
        for neighbor in graph[node]:
            if neighbor == prev:
                continue
            
            if neighbor not in visited:
                self.dfs(rank + 1, node, neighbor, lowest_rank, visited, res, graph)
                
            lowest_rank[node] = min(lowest_rank[node], lowest_rank[neighbor])
            
            if lowest_rank[neighbor] > rank:
                res.append([node, neighbor])
