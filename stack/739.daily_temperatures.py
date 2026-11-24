"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""


"""
Thought Process:
    1. Identify the pattern: Finding the "next greater element to the right"
       for every position in an array maps directly to a monotonic stack.
    2. Store indices on a decreasing stack: Keep indices of unresolved days
       whose temperatures are in non-increasing order from bottom to top.
    3. Resolve colder days on arrival: When `temperatures[curr_day]` is strictly
       greater than `temperatures[stack[-1]]`, `curr_day` is the very first
       warmer day for `stack[-1]`.
    4. Pop and compute wait distance: Pop `prev_day` and record
       `answer[prev_day] = curr_day - prev_day` until the stack is empty or
       its top temperature is >= `temperatures[curr_day]`.
    5. Push current day: Push `curr_day` onto the stack to await its own
       future warmer day (any indices left at the end stay 0 by default).

Complexity:
    Time: O(n) — each day's index is pushed once and popped at most once.
    Space: O(n) — worst-case stack size when temperatures strictly decrease.
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        res = [0] * len(temperatures)

        for curr_day, curr_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                res[prev_day] = curr_day - prev_day
            stack.append(curr_day)

        return res
        
