"""
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
Return the length of the longest (contiguous) subarray that contains only 1s. 

Example 1:
Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

Example 2:
Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

Note:
1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1 
"""


"""
Thought process:
    Find the longest subarray with at most K zeros.
"""


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        start = 0

        for end in range(len(A)):
            K -= 1 - A[end]

            if K < 0:
                K += 1 - A[start]
                start += 1

        return end - start + 1
