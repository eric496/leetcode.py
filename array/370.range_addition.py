"""
Assume you have an array of length n initialized with all 0's and are given k update operations.
Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.
Return the modified array after all k operations were executed.

Example:
Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2,0,3,5,3]
Explanation:
Initial state:
[0,0,0,0,0]
After applying operation [1,3,2]:
[0,2,2,2,0]
After applying operation [2,4,3]:
[0,2,5,5,3]
After applying operation [0,2,-2]:
[-2,0,3,5,3]
"""


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0] * (length + 1)

        for update in updates:
            res[update[0]] += update[2]
            res[update[1] + 1] -= update[2]

        for i in range(1, len(res)):
            res[i] += res[i - 1]

        res.pop()

        return res
