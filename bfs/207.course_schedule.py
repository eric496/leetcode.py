"""
There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:
Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""


# Solution 1: BFS
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        pre = defaultdict(list)
        q = deque()
        
        for x, y in prerequisites:
            indegree[x] += 1
            pre[y].append(x)
            
        for i, d in enumerate(indegree):
            if d == 0:
                q.append(i)
                
        while q:
            course = q.popleft()
            
            for nxt in pre[course]:
                indegree[nxt] -= 1
                
                if indegree[nxt] == 0:
                    q.append(nxt)
                    
        for d in indegree:
            if d:
                return False
            
        return True


# Solution 2: DFS
