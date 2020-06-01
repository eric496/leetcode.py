"""
There are N cities numbered from 1 to N.
You are given connections, where each connections[i] = [city1, city2, cost] represents the cost to connect city1 and city2 together.  (A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)
Return the minimum cost so that for every pair of cities, there exists a path of connections (possibly of length 1) that connects those two cities together.  The cost is the sum of the connection costs used. If the task is impossible, return -1.

Example 1:
Input: N = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation: 
Choosing any 2 edges will connect all cities so we choose the minimum 2.

Example 2:
Input: N = 4, connections = [[1,2,3],[3,4,4]]
Output: -1
Explanation: 
There is no way to connect all cities even if all edges are used.

Note:
1 <= N <= 10000
1 <= connections.length <= 10000
1 <= connections[i][0], connections[i][1] <= N
0 <= connections[i][2] <= 10^5
connections[i][0] != connections[i][1]
"""


class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        connections.sort(key=lambda x: x[-1])
        rank = [0] * N
        parent = list(range(N))
        res = 0
        
        for u, v, cost in connections:
            if self.union(u-1, v-1, parent, rank):
                res += cost
        
        components = set()
        
        for p in parent:
            components.add(self.find(p, parent))
            
        return res if len(components) == 1 else -1
    
    def find(self, u: int, parent: List[int]) -> int:
        if u == parent[u]:
            return u
        
        root = self.find(parent[u], parent)
        parent[u] = root
        return root
    
    def union(self, u: int, v: int, parent: List[int], rank: List[int]) -> bool:
        u_root = self.find(u, parent)
        v_root = self.find(v, parent)
        
        if u_root == v_root:
            return False
        
        if rank[u_root] > rank[v_root]:
            parent[v_root] = u_root
        elif rank[u_root] < rank[v_root]:
            parent[u_root] = v_root
        else:
            parent[v_root] = u_root
            rank[u_root] += 1
            
        return True
            