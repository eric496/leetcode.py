"""
Given an integer array A, and an integer target, return the number of tuples i, j, k  such that i < j < k and A[i] + A[j] + A[k] == target.
As the answer can be very large, return it modulo 10^9 + 7.

Example 1:
Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (A[i], A[j], A[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.

Example 2:
Input: A = [1,1,2,2,2,2], target = 5
Output: 12
Explanation: 
A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.
 
Note:
3 <= A.length <= 3000
0 <= A[i] <= 100
0 <= target <= 300
"""


# Solution 1: two pointers
class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        A.sort()
        n = len(A)
        res = 0
        
        for i in range(n-2):
            left, right = i + 1, n - 1
            
            while left < right:
                total = A[i] + A[left] + A[right]
                
                if total == target:                
                    dup1 = dup2 = 1

                    while left + dup1 < right and A[left] == A[left+dup1]:
                        dup1 += 1

                    while left < right - dup2 and A[right] == A[right-dup2]:
                        dup2 += 1
                    
                    res += (right - left + 1) * (right - left) // 2 if A[left] == A[right] else dup1 * dup2
                    left += dup1
                    right -= dup2
                elif total < target:
                    left += 1
                elif total > target:
                    right -= 1
                
        return res % (10**9 + 7)


# Solution 2: dictionary
from collections import defaultdict


class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        d1, d2 = defaultdict(int), defaultdict(int)
        res = 0

        for n in A:
            res += d2[target - n]

            for k, v in d1.items():
                d2[k + n] += v

            d1[n] += 1

        return res % (10 ** 9 + 7)
