"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Note:
The total number of elements of the given matrix will not exceed 10,000.
"""

from collections import defaultdict


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []

        if not matrix or not matrix[0]:
            return res

        diag = defaultdict(list)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                diag[row + col].append(matrix[row][col])

        for idx, ls in diag.items():
            if idx % 2:
                res.extend(ls)
            else:
                res.extend(ls[::-1])

        return res
