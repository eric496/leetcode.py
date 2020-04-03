"""
Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].
After this process, we have some array B.
Return the smallest possible difference between the maximum value of B and the minimum value of B.

Example 1:
Input: A = [1], K = 0
Output: 0
Explanation: B = [1]

Example 2:
Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]

Example 3:
Input: A = [1,3,6], K = 3
Output: 0
Explanation: B = [3,3,3] or B = [4,4,4]
 
Note:
1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000
"""

"""
Thought process:
    1. Find the max and min values of the array, we want to minimize the range between them because they form the current largest range of the array.
    2. Add K to the min and subtract K from the max, if the results overlap, we know the smallest range is 0 after the operations.
       If not overlapping, return the gap between (max - K) and (min + K)
"""


class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        min_, max_ = min(A), max(A)

        return 0 if max_ - K <= min_ + K else max_ - K - (min_ + K)
