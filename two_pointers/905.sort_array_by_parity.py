"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
You may return any answer array that satisfies this condition.

Example 1:
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Note:
1 <= A.length <= 5000
0 <= A[i] <= 5000
"""


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        lo, hi = 0, len(A) - 1
        
        while lo < hi:
            if A[lo] & 1 and not A[hi] & 1:
                A[lo], A[hi] = A[hi], A[lo]
            elif not A[lo] & 1:
                lo += 1
            elif A[hi] & 1:
                hi -= 1
                
        return A
