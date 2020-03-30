"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""


# Solution 1: backward traversal
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stk = []
        res = [0] * len(T)
        
        for i in range(len(T)-1, -1, -1):
            if not stk:
                stk.append((T[i], i))
            else:
                while stk and stk[-1][0] <= T[i]:
                    stk.pop()
                
                if stk:
                    res[i] = stk[-1][1] - i
                
                stk.append((T[i], i))
                
        return res


# Solution 2: forward traversal
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stk = []
        
        for i, t in enumerate(T):
            while stk and T[stk[-1]] < t:
                top = stk.pop()
                res[top] = i - top

            stk.append(i)
        
        return res
