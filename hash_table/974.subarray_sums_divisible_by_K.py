"""
Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

Example 1:
Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Note:
1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
"""


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        res = accsum = 0
        mod_d = {0:1}
        
        for n in A:
            accsum += n
            if accsum%K in mod_d:
                res += mod_d[accsum%K]
                mod_d[accsum%K] += 1
            else:
                mod_d[accsum%K] = 1
        
        return res
        