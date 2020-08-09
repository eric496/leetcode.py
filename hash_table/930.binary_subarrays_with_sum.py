"""
In an array A of 0s and 1s, how many non-empty subarrays have sum S?

Example 1:
Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation: 
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Note:
A.length <= 30000
0 <= S <= A.length
A[i] is either 0 or 1.
"""


# Solution 1: hash table - similar to 2sum, O(n) SC
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        presum = {0: 1}
        res = cumsum = 0

        for n in A:
            cumsum += n
            res += presum.get(cumsum - S, 0)
            presum[cumsum] = presum.get(cumsum, 0) + 1

        return res


# Solution 2: two pointers - O(1) SC
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        return self.numSubarrayLessEqualSum(A, S) - self.numSubarrayLessEqualSum(A, S - 1)
        
        
    def numSubarrayLessEqualSum(self, A: List[int], S: int) -> int:
        lo = hi = 0
        res = 0
        cursum = 0
        
        while hi < len(A):
            cursum += A[hi]
            
            while lo <= hi and cursum > S:
                cursum -= A[lo]
                lo += 1
                
            res += hi - lo + 1
            hi += 1
            
        return res
        