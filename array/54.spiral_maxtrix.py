"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


"""
Thought Process:
    1. Define 4 shrinking walls: Track `top = 0`, `bottom = m - 1`,
       `left = 0`, and `right = n - 1` to bound the unvisited submatrix.
    2. Traverse 4 edges per layer:
       - Top row (`left` to `right`), then shrink `top += 1`.
       - Right column (`top` to `bottom`), then shrink `right -= 1`.
       - Bottom row (`right` to `left`), then shrink `bottom -= 1`.
       - Left column (`bottom` to `top`), then shrink `left += 1`.
    3. Guard against duplicate reads on non-square leftovers: After moving `top`
       and `right` inward, verify `top <= bottom` before scanning the bottom row,
       and `left <= right` before scanning the left column (prevents re-reading a
       single remaining row or column).
    4. Terminate when walls cross: Stop once `top > bottom` or `left > right`.

Complexity:
    Time: O(m * n) — every cell is visited and appended once.
    Space: O(1) extra space (excluding the output list).
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        res = []

        while top <= bottom and left <= right:
            # 1. Traverse left -> right along the top wall
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            # 2. Traverse top -> bottom along the right wall
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            # 3. Traverse right -> left along the bottom wall (if rows remain)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1

            # 4. Traverse bottom -> top along the left wall (if cols remain)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res
