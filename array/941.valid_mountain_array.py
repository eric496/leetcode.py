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
            elif i == len(A) - 1:
                if A[-1] >= A[-2]:
                    return False
            elif A[i - 1] <= A[i] and A[i] >= A[i + 1]:
                cnt_peaks += 1

        return True if cnt_peaks == 1 else False


# Solution 2: Two pointers
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        left, right = 0, n - 1

        while left + 1 < n and arr[left] < arr[left+1]:
            left += 1

        while right - 1 > 0 and arr[right] < arr[right-1]:
            right -= 1

        return left != n - 1 and right != 0 and left == right 
