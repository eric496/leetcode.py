"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""


# Solution 1: Brute force - O(n^2) TC and O(1) SC
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        for i in range(1, len(height) - 1):
            shortest_bar = min(max(height[:i]), max(height[i:]))

            if shortest_bar > height[i]:
                res += shortest_bar - height[i]

        return res


# Solution 2: DP
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        max_left[0] = height[0]
        max_right[-1] = height[-1]

        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i])

        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])

        res = 0

        for i, h in enumerate(height):
            lower_bound = min(max_left[i], max_right[i])
            res += lower_bound - h

        return res


# Solution 3: two pointers - O(n) TC and O(1) SC
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left_max = right_max = 0
        start, end = 0, len(height) - 1

        while start < end:
            left_max = max(left_max, height[start])
            right_max = max(right_max, height[end])

            if left_max < right_max:
                res += left_max - height[start]
                start += 1
            else:
                res += right_max - height[end]
                end -= 1

        return res
