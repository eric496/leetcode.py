"""
There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.
The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.
Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

Example 1:
Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.

Example 2:
Input: heights = [4,3,2,1]
Output: [0,1,2,3]
Explanation: All the buildings have an ocean view.

Example 3:
Input: heights = [1,3,2,4]
Output: [3]
Explanation: Only building 3 has an ocean view.

Constraints:
1 <= heights.length <= 105
1 <= heights[i] <= 109
"""


"""
Thought Process:
    1. Define the ocean-view condition: Building `i` sees the ocean if and only
       if `heights[i]` is strictly greater than every building to its right
       (`heights[i] > max(heights[i + 1:])`).
    2. Scan right-to-left with a running maximum: Initialize `max_height = 0`
       (since all heights >= 1) and iterate from `n - 1` down to `0`.
    3. Collect valid indices: Whenever `heights[i] > max_height`, append `i`
       to `result` and update `max_height = heights[i]`.
    4. Reverse at the end: Since indices are collected in decreasing order,
       reverse `result` in-place (`result.reverse()`) to return them sorted.

Complexity:
    Time: O(n) — single right-to-left scan plus O(n) in-place reversal.
    Space: O(1) extra space (excluding the output list).
"""


from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_height = 0
        result = []

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_height:
                result.append(i)
                max_height = heights[i]

        result.reverse()
        return result


"""
Thought Process:
    1. Scan left-to-right with a monotonic stack: Maintain `stack` holding
       indices of buildings whose heights are strictly decreasing from bottom
       to top.
    2. Evict blocked buildings: Before pushing index `i`, pop every index
       `stack[-1]` where `heights[stack[-1]] <= heights[i]` because building
       `i` blocks their view of the ocean to the right.
    3. Push current building: Append `i` onto `stack` as a valid candidate.
    4. Return directly: Every surviving index in `stack` has no taller or
       equal building to its right, and indices are already in ascending order.

Complexity:
    Time: O(n) — each index is pushed once and popped at most once.
    Space: O(n) — auxiliary stack holds up to n indices in the worst case.
"""


from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []

        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] <= height:
                stack.pop()
            stack.append(i)

        return stack
      
