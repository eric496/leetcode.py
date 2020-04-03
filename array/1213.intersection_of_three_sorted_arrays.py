"""
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

Example 1:
Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.

Constraints:
1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000
"""


# Hash table
class Solution:
    def arraysIntersection(
        self, arr1: List[int], arr2: List[int], arr3: List[int]
    ) -> List[int]:
        freq = {}

        for n in arr1:
            freq[n] = freq.get(n, 0) + 1

        for n in arr2:
            freq[n] = freq.get(n, 0) + 1

        for n in arr3:
            freq[n] = freq.get(n, 0) + 1

        res = []

        for k, v in freq.items():
            if v == 3:
                res.append(k)

        return res


# Three pointers
class Solution:
    def arraysIntersection(
        self, arr1: List[int], arr2: List[int], arr3: List[int]
    ) -> List[int]:
        i = j = k = 0
        res = []

        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                res.append(arr1[i])
                i, j, k = i + 1, j + 1, k + 1
                continue

            max_ = max(arr1[i], arr2[j], arr3[k])
            i = i + 1 if arr1[i] < max_ else i
            j = j + 1 if arr2[j] < max_ else j
            k = k + 1 if arr3[k] < max_ else k

        return res
