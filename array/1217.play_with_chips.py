"""
There are some chips, and the i-th chip is at position chips[i].
You can perform any of the two following types of moves any number of times (possibly zero) on any chip:
Move the i-th chip by 2 units to the left or to the right with a cost of 0.
Move the i-th chip by 1 unit to the left or to the right with a cost of 1.
There can be two or more chips at the same position initially.
Return the minimum cost needed to move all the chips to the same position (any position).

Example 1:
Input: chips = [1,2,3]
Output: 1
Explanation: Second chip will be moved to positon 3 with cost 1. First chip will be moved to position 3 with cost 0. Total cost is 1.

Example 2:
Input: chips = [2,2,2,3,3]
Output: 2
Explanation: Both fourth and fifth chip will be moved to position two with cost 1. Total minimum cost will be 2.
 
Constraints:
1 <= chips.length <= 100
1 <= chips[i] <= 10^9
"""

"""
Thought process:
    Moving from an even position to another even or moving from an odd to an odd is free.
    Untimately we need to move all chips to the same position, which means we either
    move all even-positioned to an odd position or all odd-positioned to an even position 
    whichever operation is cheaper.
"""


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = even = 0
        
        for p in position:
            if p & 1:
                even += 1
            else:
                odd += 1
        
        return min(odd, even)
