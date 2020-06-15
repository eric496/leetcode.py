"""
Given an integer n. Each number from 1 to n is grouped according to the sum of its digits. 
Return how many groups have the largest size.

Example 1:
Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups with largest size.

Example 2:
Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.

Example 3:
Input: n = 15
Output: 6

Example 4:
Input: n = 24
Output: 5

Constraints:
1 <= n <= 10^4
"""


from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(list)

        for i in range(1, n + 1):
            cur = i
            sum_ = 0

            while cur:
                sum_ += cur % 10
                cur //= 10

            groups[sum_].append(i)

        res = 1
        max_size = 0

        for v in groups.values():
            if len(v) > max_size:
                res = 1
                max_size = len(v)
            elif len(v) == max_size:
                res += 1

        return res
