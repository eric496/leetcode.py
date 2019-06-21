"""
Given an array A of integers, return true if and only if it is a valid mountain array.
Recall that A is a mountain array if and only if:
A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]

Example 1:
Input: [2,1]
Output: false

Example 2:
Input: [3,5,5]
Output: false

Example 3:
Input: [0,3,2,1]
Output: true

Note:
0 <= A.length <= 10000
0 <= A[i] <= 10000 
"""

# Solution 1: count the number of peaks
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        
        cnt_peaks = 0
        
        for i in range(len(A)):
            if i == 0:
                if A[0] >= A[1]:
                    return False
            elif i == len(A)-1: 
                if A[-1] >= A[-2]:
                    return False
            elif A[i-1] <= A[i] and A[i] >= A[i+1]:
                cnt_peaks += 1
        
        return True if cnt_peaks == 1 else False


# Solution 2: Two pointers
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        
        i, j = 0, len(A)-1
        
        while i + 1 < len(A) and A[i] < A[i+1]:
            i += 1
        
        while j - 1 >= 0 and A[j] < A[j-1]:
            j -= 1
        
        return i > 0 and j < len(A)-1 and i == j
        