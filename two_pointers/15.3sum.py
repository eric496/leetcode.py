"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


# Solution 0: Brute force - 3 nested loops - O(n^3) TC


# Solution 1: fixed one element and use two pointers
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res = set()
        nums.sort()

        for i in range(n - 2):
            if nums[i] > 0:
                break

            left = i + 1
            right = n - 1

            while left < right:
                val = nums[i] + nums[left] + nums[right]
                if val == 0:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif val > 0:
                    right -= 1
                elif val < 0:
                    left += 1
            
        return list(map(list, res))


# Solution 2: dedup using set and tuple
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_nums = sorted(nums)
        i = 0
        n = len(sorted_nums)
        res = set()

        while i < n - 2:
            if sorted_nums[i] > 0:
                break
            while 0 < i < n - 2 and sorted_nums[i] == sorted_nums[i-1]:
                i +=1
            j, k = i + 1, n - 1
            while j < k:
                val = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
                if val == 0:
                    res.add((sorted_nums[i], sorted_nums[j], sorted_nums[k]))
                    j += 1
                    k -= 1
                elif val < 0:
                    j += 1
                else:
                    k -= 1
            i += 1
        
        return list(map(list, res))


# Solution 3: two pointers - O(n^2) TC and O(1) SC
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            lo, hi = i + 1, n - 1

            while lo < hi:
                total = nums[i] + nums[lo] + nums[hi]

                if total == 0:
                    res.append([nums[i], nums[lo], nums[hi]])

                    # Skip duplicates
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1

                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1

                    lo += 1
                    hi -= 1
                elif total < 0:
                    lo += 1
                elif total > 0:
                    hi -= 1

        return res
