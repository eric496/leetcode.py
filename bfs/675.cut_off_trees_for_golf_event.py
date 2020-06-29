"""
You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:
0 represents the obstacle can't be reached.
1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.
In one step you can walk in any of the four directions top, bottom, left and right also when standing in a point which is a tree you can decide whether or not to cut off the tree.
You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1).
You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. If you can't cut off all the trees, output -1 in that situation.
You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

Example 1:
Input: 
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
Output: 6
 
Example 2:
Input: 
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
Output: -1

Example 3:
Input: 
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
Output: 6
Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.

Constraints:
1 <= forest.length <= 50
1 <= forest[i].length <= 50
0 <= forest[i][j] <= 10^9
"""


from collections import deque

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if not forest or not forest[0]:
            return -1
        
        trees = []
        m, n = len(forest), len(forest[0])
        
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], i, j))
                
        trees.sort()
        trees = deque(trees)
        res = 0
        start_y = start_x = 0
        
        while trees:
            _, y, x = trees.popleft()
            step = self.bfs(forest, start_y, start_x, y, x)
            
            if step == -1:
                return -1
            
            res += step
            start_y, start_x = y, x
            
        return res
            
    def bfs(self, forest: List[List[int]], start_y: int, start_x: int, y: int, x: int) -> int:
        q = deque([(start_y, start_x)])
        visited = {(start_y, start_x)}
        step = 0
        
        while q:
            for _ in range(len(q)):
                cur_y, cur_x = q.popleft()
                
                if cur_y == y and cur_x == x:
                    return step
                
                for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_y, new_x = cur_y + dy, cur_x + dx
                    
                    if 0 <= new_y < len(forest) and 0 <= new_x < len(forest[0]) and (new_y, new_x) not in visited and forest[new_y][new_x] != 0:
                        q.append((new_y, new_x))
                        visited.add((new_y, new_x))
                        
            step += 1
            
        return -1
                        