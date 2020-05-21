"""
Given an array of integers arr.
We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).
Let's define a and b as follows:
a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.
Return the number of triplets (i, j and k) Where a == b.

Example 1:
Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)

Example 2:
Input: arr = [1,1,1,1,1]
Output: 10

Example 3:
Input: arr = [2,3]
Output: 0

Example 4:
Input: arr = [1,3,5,7,9]
Output: 3

Example 5:
Input: arr = [7,11,12,9,5,2,7,17,22]
Output: 8

Constraints:
1 <= arr.length <= 300
1 <= arr[i] <= 10^8
"""


# Solution 1: O(n^2) TC 
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prexor = {0: [-1]}
        cur = res = 0
        
        for i, n in enumerate(arr):
            cur ^= n
            
            if cur in prexor:
                for pre in prexor[cur]:
                    res += i - pre - 1
                prexor[cur].append(i)
            else:
                prexor[cur] = [i]
        
        return res
            
        
# Solution 2: O(n) TC
# (i -a -1) + (i - b - 1) + (i - c - 1) = i * 3 - (a + b + c) - 3
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prexor = {0: (-1, 1)}
        cur = res = 0
        
        for i, n in enumerate(arr):
            cur ^= n
            presum, cnt = prexor.get(cur, (0, 0))
            res += i * cnt - presum - cnt
            prexor[cur] = (presum + i, cnt + 1)
        
        return res
            