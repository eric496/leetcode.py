"""
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
Each person may dislike some other people, and they should not go into the same group. 
Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.
Return true if and only if it is possible to split everyone into two groups in this way.

Example 1:
Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]

Example 2:
Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false

Example 3:
Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false

Note:
1 <= N <= 2000
0 <= dislikes.length <= 10000
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].
"""


from collections import defaultdict


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        enemies = defaultdict(list)
        
        for a, b in dislikes:
            enemies[a].append(b)
            enemies[b].append(a)
            
        colors = [0] * (N + 1)
        
        for i in range(1, N + 1):
            if colors[i] == 0:
                if not self.dfs(i, 1, colors, enemies):
                    return False
                
        return True
    
    def dfs(self, n: int, color: int, colors: List[int], enemies: dict) -> bool:
        colors[n] = color
        
        for enemy in enemies[n]:
            if colors[enemy] == color:
                return False
            
            if colors[enemy] == 0:
                if not self.dfs(enemy, -color, colors, enemies):
                    return False
        
        return True
        