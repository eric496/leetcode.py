"""
Given a picture consisting of black and white pixels, find the number of black lonely pixels.
The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.
A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

Example:
Input: 
[['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]
Output: 3
Explanation: All the three 'B's are black lonely pixels.

Note:
The range of width and height of the input 2D array is [1,500].
"""


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m, n = len(picture), len(picture[0])
        row_cnt, col_cnt = [0] * m, [0] * n

        for i in range(m):
            for j in range(n):
                if picture[i][j] == "B":
                    row_cnt[i] += 1
                    col_cnt[j] += 1

        cnt = 0

        for i in range(m):
            for j in range(n):
                if picture[i][j] == "B" and row_cnt[i] == 1 and col_cnt[j] == 1:
                    cnt += 1

        return cnt
