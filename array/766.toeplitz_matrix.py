"""
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
 
Example 1:
Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.

Example 2:
Input:
matrix = [
  [1,2],
  [2,2]
]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.

Note:
matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].

Follow up:
What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
What if the matrix is so large that you can only load up a partial row into the memory at once?
"""


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])

        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] != matrix[r-1][c-1]:
                    return False

        return True 


# Follow up 1
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        prev_r = matrix[0]

        for r in range(1, m):
            curr_r = matrix[r]

            for c in range(1, n):
                if prev_r[c-1] != curr_r[c]:
                    return False

            prev_r = curr_r

        return True
      
  
# Follow up 2
"""
If the matrix is so massive (e.g., billions of columns) that even a single row exceeds memory limits, you have to process the matrix in overlapping vertical slices or chunks. This shifts the problem from a pure algorithm question to a systems engineering challenge involving streaming and disk I/O.
The Strategy (Chunking):
    - Define a Chunk Size: Determine a chunk_size that safely fits into memory (e.g., k elements).
    - Process by Columns: Logically divide the matrix into vertical slices (Columns 0 to k, k−1 to 2k−1, etc.). Note the overlap of 1 column between chunks, which is necessary to maintain the diagonal check across chunk boundaries.
    - Stream Downward: For each vertical slice, stream the data row by row from disk. You only need to hold prev_chunk and curr_chunk in memory at any given time.

Conceptual Execution:
    Read Row 0, Cols [0:k]. Store as prev_chunk.
    Read Row 1, Cols [0:k]. Store as curr_chunk.
    Compare curr_chunk[1:] with prev_chunk[:-1].
    Set prev_chunk = curr_chunk.
    Read Row 2, Cols [0:k]... and so on until the bottom of the matrix.
    Once finished with the first vertical slice, move to the next slice: Cols [k-1:2k-1], and repeat the downward stream.
    Space Complexity: O(k) where k is the defined chunk size.
    Trade-off: This approach minimizes memory footprint but requires reading the entire matrix from disk multiple times (once for each vertical slice), heavily increasing disk I/O operations.
"""
