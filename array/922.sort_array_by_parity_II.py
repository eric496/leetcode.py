"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
You may return any answer array that satisfies this condition.

Example 1:
Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

Note:
2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
"""


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        if not A or len(A) < 2:
            return A

        even, odd = 0, 1
        len_A = len(A)

        while even < len_A and odd < len_A:
            # Skip all qualified even-indexed elements
            while even < len_A and A[even] & 1 == 0:
                even += 2

            # Skip all qualified odd-indexed elements
            while odd < len_A and A[odd] & 1 == 1:
                odd += 2

            # Test the condition that the indices are in the range!
            if even < len_A and odd < len_A:
                A[even], A[odd] = A[odd], A[even]

            even += 2
            odd += 2

        return A
