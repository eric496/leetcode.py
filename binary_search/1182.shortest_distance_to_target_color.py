"""
You are given an array colors, in which there are three colors: 1, 2 and 3.
You are also given some queries. Each query consists of two integers i and c, return the shortest distance between the given index i and the target color c. If there is no solution return -1.

Example 1:
Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
Output: [3,0,3]
Explanation: 
The nearest 3 from index 1 is at index 4 (3 steps away).
The nearest 2 from index 2 is at index 2 itself (0 steps away).
The nearest 1 from index 6 is at index 3 (3 steps away).

Example 2:
Input: colors = [1,2], queries = [[0,3]]
Output: [-1]
Explanation: There is no 3 in the array.

Constraints:
1 <= colors.length <= 5*10^4
1 <= colors[i] <= 3
1 <= queries.length <= 5*10^4
queries[i].length == 2
0 <= queries[i][0] < colors.length
1 <= queries[i][1] <= 3
"""


from collections import defaultdict

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        pos = defaultdict(list)
        
        for i, c in enumerate(colors):
            pos[c].append(i)
            
        res = []    
        
        for i, c in queries:
            if c in pos:
                ix = self.lower_bound(pos[c], i)
                
                if ix == len(pos[c]):
                    res.append(abs(i - pos[c][-1]))
                elif ix == 0:
                    res.append(abs(i - pos[c][0]))
                else:
                    res.append(min(abs(pos[c][ix]-i), abs(pos[c][ix-1]-i)))
            else:
                res.append(-1)
            
        return res
        
    def lower_bound(self, indices: List[int], i: int) -> int:
        lo, hi = 0, len(indices)
        
        while lo < hi:
            mid = lo + (hi - lo >> 1)
            
            if indices[mid] >= i:
                hi = mid
            else:
                lo = mid + 1
                
        return lo  
        