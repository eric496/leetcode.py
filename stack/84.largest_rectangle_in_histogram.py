"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Example:
Input: [2,1,5,6,2,3]
Output: 10
"""

# Solution 1: Two arrays
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n, max_area = len(heights), 0
        left, right = [1]*n, [1]*n
        
        for i in range(n):
            j = i - 1
            while j >= 0:
                if heights[j] >= heights[i]:
                    left[i] += left[j]
                    j -= left[j]
                else:
                    break
        
        for i in range(n-1, -1, -1):
            j = i + 1
            while j < n:
                if heights[j] >= heights[i]:
                    right[i] += right[j]
                    j += right[j]
                else:
                    break
        
        for i in range(n):
            max_area = max(max_area, heights[i]*(left[i]+right[i]-1))
            
        return max_area

# Solution 2: Stack
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stk = [-1]
        max_area = 0
        
        for i in range(len(heights)):
            while heights[i] < heights[stk[-1]]:
                h = heights[stk.pop()]
                w = i - stk[-1] - 1
                max_area = max(max_area, h*w)
            stk.append(i)
        
        return max_area
