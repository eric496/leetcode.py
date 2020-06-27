"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.
At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.

Note:
The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
"""


# Solution 1: DFS
class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, new_color: int
    ) -> List[List[int]]:
        if not image or not image[0]:
            return []

        old_color = image[sr][sc]
        visited = set()
        self.dfs(image, sr, sc, old_color, new_color, visited)

        return image

    def dfs(
        self,
        image: List[List[int]],
        y: int,
        x: int,
        old_color: int,
        new_color: int,
        visited: set,
    ) -> None:
        if (
            0 <= y < len(image)
            and 0 <= x < len(image[0])
            and (y, x) not in visited
            and image[y][x] == old_color
        ):
            image[y][x] = new_color
            visited.add((y, x))

            for dy, dx in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                self.dfs(image, y + dy, x + dx, old_color, new_color, visited)


# Solution 2: BFS
from collections import deque


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, new_color: int
    ) -> List[List[int]]:
        if not image or not image[0]:
            return []

        m, n = len(image), len(image[0])
        q = deque([(sr, sc)])
        visited = set()
        old_color = image[sr][sc]

        while q:
            for _ in range(len(q)):
                y, x = q.popleft()
                image[y][x] = new_color
                visited.add((y, x))

                for dy, dx in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    new_y, new_x = y + dy, x + dx

                    if (
                        0 <= new_y < m
                        and 0 <= new_x < n
                        and (new_y, new_x) not in visited
                        and image[new_y][new_x] == old_color
                    ):
                        q.append((y + dy, x + dx))

        return image
