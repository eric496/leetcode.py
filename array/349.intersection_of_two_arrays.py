'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
'''

# O(mn) time complexity
class Solution:
    def intersection(self, nums1: list, nums2: list) -> list:
        res = []
        for n in nums1:
            if n in nums2:
                res.append(n)
                nums2.remove(n)
        return list(set(res))

# sort first, max(O(nlogn), O(mlogm)) time complexity
class Solution:
    def intersection(self, nums1: list, nums2: list) -> list:
        res = []
        nums1.sort()
        nums2.sort()
        p1 = p2 = 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                if nums1[p1] not in res:
                    res.append(nums1[p1])
                    p1 += 1
                    p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return res
