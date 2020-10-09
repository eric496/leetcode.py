"""
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:
B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)
Given an array A of integers, return the length of the longest mountain. 
Return 0 if there is no mountain.

Example 1:
Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:
Input: [2,2,2]
Output: 0
Explanation: There is no mountain.

Note:
0 <= A.length <= 10000
0 <= A[i] <= 10000

Follow up:
Can you solve it using only one pass?
Can you solve it in O(1) space?
"""


# Solution 1: two passes
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        
        n = len(A)
        ups, downs = [0] * n, [0] * n
        i, j = 0, n - 1
        
        while i < n - 1:
            if A[i] < A[i+1]:
                ups[i+1] = ups[i] + 1
                
            i += 1
        
        while j > 0:
            if A[j] < A[j-1]:
                downs[j-1] = downs[j] + 1
                
            j -= 1
        
        longest = [u + d + 1 for u, d in zip(ups, downs) if u and d]
        
        return max(longest) if longest else 0


# Solution 2: one pass, two pinters
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        res = 0
        ups = downs = 0
        i = 0
        n = len(A)
        
        while i < n - 1:
            if downs and A[i] < A[i+1] or A[i] == A[i+1]:
                ups = downs = 0
                
            if A[i] < A[i+1]:
                ups += 1
                
            if A[i] > A[i+1]:
                downs += 1
                
            if ups and downs:
                res = max(res, ups + downs + 1)
                
            i += 1
                
        return res
