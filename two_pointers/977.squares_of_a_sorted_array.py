"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Note:
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
"""


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        start, end = 0, len(A) - 1
        ptr = len(A) - 1
        res = [0] * len(A)

        while start <= end:
            if abs(A[start]) > abs(A[end]):
                res[ptr] = A[start] ** 2
                start += 1
            else:
                res[ptr] = A[end] ** 2
                end -= 1
            ptr -= 1

        return res
