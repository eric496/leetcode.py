"""
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
You can swap the characters at any pair of indices in the given pairs any number of times.
Return the lexicographically smallest string that s can be changed to after using the swaps.

Example 1:
Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"

Example 2:
Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"

Example 3:
Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination: 
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"

Constraints:
1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s only contains lower case English letters.
"""


from collections import defaultdict

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = list(range(n))
        rank = [0] * n
        
        for u, v in pairs:
            self.union(u, v, parent, rank)
        
        offsprings = defaultdict(list)
        
        for i, p in enumerate(parent):
            offsprings[self.find(p, parent)].append(i)
            
        order = {}
        
        for indices in offsprings.values():
            vals = [s[i] for i in indices]
            
            for c, i in zip(sorted(vals), sorted(indices)):
                order[i] = c
                
        res = [""] * n
        
        for k, v in order.items():
            res[k] = v
            
        return "".join(res)
            
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
            