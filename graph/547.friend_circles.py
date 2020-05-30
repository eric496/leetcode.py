"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.
Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.

Example 2:
Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.
"""


# Solution 1: DFS
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        visited = [0] * len(M)
        cnt = 0

        for i in range(len(M)):
            if not visited[i]:
                self.dfs(M, visited, i)
                cnt += 1

        return cnt

    def dfs(self, M: List[List[int]], visited: List[int], person: int) -> None:
        for friend in range(len(M)):
            if M[person][friend] == 1 and not visited[friend]:
                visited[friend] = 1
                self.dfs(M, visited, friend)


# Solution 2: Union Find without optimization
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        parent = list(range(n))
        
        for i in range(n):
            for j in range(i+1, n):
                if M[i][j] == 1:
                    self.union(i, j, parent)
                    
        res = set()
        
        for i in range(n):
            res.add(self.find(i, parent))
            
        return len(res)
        
    def find(self, p: int, parent: List[int]) -> int:
        return p if parent[p] == p else self.find(parent[p], parent)
    
    def union(self, p: int, q: int, parent: List[int]) -> None:
        p_root = self.find(p, parent)
        q_root = self.find(q, parent)
        parent[p_root] = q_root


# Solution 3: Union Find with path compression and union by rank
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        parent = list(range(n))
        rank = [0] * n
        
        for i in range(n):
            for j in range(i+1, n):
                if M[i][j] == 1:
                    self.union(i, j, parent, rank)
         
        res = set()
        
        for p in parent:
            res.add(self.find(p, parent))
            
        return len(res)
        
    def find(self, p: int, parent: List[int]) -> int:
        # while p != parent[p]:
        #     parent[p] = parent[parent[p]]
        #     p = parent[p]
            
        # return p
        if p != parent[p]:
            root = self.find(parent[p], parent)
            parent[p] = root
            return root
        else:
            return p
        
    def union(self, p: int, q: int, parent: List[int], rank: List[int]) -> None:
        p_root = self.find(p, parent)
        q_root = self.find(q, parent)
        
        if rank[p_root] > rank[q_root]:
            parent[q_root] = p_root
        elif rank[p_root] < rank[q_root]:
            parent[p_root] = q_root
        else:
            parent[q_root] = p_root
            rank[p_root] += 1
            