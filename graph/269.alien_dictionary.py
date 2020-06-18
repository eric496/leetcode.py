"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:
Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
Output: "wertf"

Example 2:
Input:
[
  "z",
  "x"
]
Output: "zx"

Example 3:
Input:
[
  "z",
  "x",
  "z"
] 
Output: "" 
Explanation: The order is invalid, so return "".

Note:
You may assume all letters are in lowercase.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""


# Solution: Topo sort
from collections import defaultdict
from collections import deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if not words:
            return ""
        
        if len(words) == 1:
            return words[0]
        
        graph = defaultdict(set)
        indegrees = defaultdict(int)
        
        for word in words:
            for c in word:
                indegrees[c] = 0
        
        for i in range(1, len(words)):
            if len(words[i-1]) > len(words[i]) and words[i-1].startswith(words[i]):
                return ""
            
            size = min(len(words[i-1]), len(words[i]))
            
            for j in range(size):
                first, second = words[i-1][j], words[i][j]
                
                if first != second:
                    if second not in graph[first]:
                        graph[first].add(second)
                        indegrees[second] += 1
                    
                    break
        
        q = deque()
        
        for c, cnt in indegrees.items():
            if cnt == 0:
                q.append(c)
                
        res = []
            
        while q:
            c = q.popleft()
            res.append(c)
            
            for nxt in graph[c]:
                indegrees[nxt] -= 1
                
                if indegrees[nxt] == 0:
                    q.append(nxt)
                    
        return "".join(res) if len(res) == len(indegrees) else ""
    