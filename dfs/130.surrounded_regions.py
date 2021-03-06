"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X
Explanation:
Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""


# Solution 1: DFS
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return board

        m, n = len(board), len(board[0])
        visited = set()

        for i in range(m):
            self.dfs(i, 0, board, visited)
            self.dfs(i, n - 1, board, visited)

        for j in range(n):
            self.dfs(0, j, board, visited)
            self.dfs(m - 1, j, board, visited)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "*":
                    board[i][j] = "O"

    def dfs(self, i: int, j: int, board: List[List[str]], visited: set) -> None:
        if (
            0 <= i < len(board)
            and 0 <= j < len(board[0])
            and (i, j) not in visited
            and board[i][j] == "O"
        ):
            visited.add((i, j))
            board[i][j] = "*"

            for dy, dx in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                self.dfs(i + dy, j + dx, board, visited)


# Solution 2: BFS
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return board

        m, n = len(board), len(board[0])
        q = deque()
        visited = set()

        for i in range(m):
            if board[i][0] == "O" and (i, 0) not in visited:
                board[i][0] = "#"
                q.append((i, 0))
                visited.add((i, 0))

            if board[i][n - 1] == "O" and (i, n - 1) not in visited:
                board[i][n - 1] = "#"
                q.append((i, n - 1))
                visited.add((i, n - 1))

        for i in range(n):
            if board[0][i] == "O" and (0, i) not in visited:
                board[0][i] = "#"
                q.append((0, i))
                visited.add((0, i))

            if board[m - 1][i] == "O" and (m - 1, i) not in visited:
                board[m - 1][i] = "#"
                q.append((m - 1, i))
                visited.add((m - 1, i))

        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

        while q:
            for _ in range(len(q)):
                y, x = q.popleft()

                for dy, dx in directions:
                    y1, x1 = y + dy, x + dx

                    if (
                        0 <= y1 < m
                        and 0 <= x1 < n
                        and board[y1][x1] == "O"
                        and (y1, x1) not in visited
                    ):
                        board[y1][x1] = "#"
                        q.append((y1, x1))
                        visited.add((y1, x1))

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
