"""
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].
A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

Example 1:
Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]

Example 2:
Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]

Constraints:
    -300 <= x, y <= 300
    0 <= |x| + |y| <= 300
"""


from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        queue = deque([(0, 0, 0)])
        visited = {(0, 0)}
        ds = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

        while queue:
            r, c, steps = queue.popleft()
            
            if r == x and c == y:
                return steps

            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in visited:
                    queue.append((nr, nc, steps+1))
                    visited.add((nr, nc))
