"""
On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.
Now, a move consists of removing a stone that shares a column or row with another stone on the grid.
What is the largest possible number of moves we can make?

Example 1:
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5

Example 2:
Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3

Example 3:
Input: stones = [[0,0]]
Output: 0

Note:
1 <= stones.length <= 1000
0 <= stones[i][j] < 10000
"""


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parent = list(range(n))
        rank = [0] * n
        
        for i in range(n):
            for j in range(i+1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    self.union(i, j, parent, rank)
                    
        components = set()
        
        for p in parent:
            components.add(self.find(p, parent))
        
        return n - len(components)

    def find(self, u: int, parent: List[int]) -> int:
        if u == parent[u]:
            return u
        else:
            root = self.find(parent[u], parent)
            parent[u] = root
            return root
    
    def union(self, u: int, v: int, parent: List[int], rank: List[int]) -> None:
        u_root = self.find(u, parent)
        v_root = self.find(v, parent)
        
        if u_root == v_root:
            return
        
        if rank[u_root] > rank[v_root]:
            parent[v_root] = u_root
        elif rank[u_root] < rank[v_root]:
            parent[u_root] = v_root
        else:
            parent[v_root] = u_root
            rank[u_root] += 1
