"""
Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.
What is the most number of chunks we could have made?

Example 1:
Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.

Example 2:
Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.

Note:
arr will have length in range [1, 10].
arr[i] will be a permutation of [0, 1, ..., arr.length - 1].
"""


# Method 1
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        max_left, min_right = [arr[0]] + [0] * (n - 1), [0] * (n - 1) + [arr[n - 1]]

        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], arr[i])

        for i in range(n - 2, -1, -1):
            min_right[i] = min(min_right[i + 1], arr[i])

        res = 0

        for i in range(n - 1):
            if max_left[i] <= min_right[i + 1]:
                res += 1

        return res + 1


# Method 2
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = curmax = 0

        for i, n in enumerate(arr):
            curmax = max(curmax, n)
            res = res + 1 if curmax == i else res

        return res
