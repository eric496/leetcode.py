"""
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.
Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.
Could you do this in O(n) runtime?

Example:
Input: [3, 10, 5, 25, 2, 8]
Output: 28
Explanation: The maximum result is 5 ^ 25 = 28.
"""


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        mask = 0
        res = 0

        for i in range(31, -1, -1):
            mask = mask | (1 << i)
            lookup = set()

            for num in nums:
                left = num & mask
                lookup.add(left)

            want = res | (1 << i)

            for n in lookup:
                m = n ^ want

                if m in lookup:
                    res = want
                    break

        return res
