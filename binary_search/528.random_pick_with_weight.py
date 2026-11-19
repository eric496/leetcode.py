"""
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:
1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.

Example 1:
Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]

Example 2:
Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]

Explanation of Input Syntax:
The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""


"""
Thought Process:
    1. Model probabilities as intervals: Lay each weight `w[i]` end-to-end
       on a number line so index `i` spans a bucket of width `w[i]`.
    2. Build prefix sums: Store cumulative weights so `prefix_sums[i]`
       marks the right endpoint of bucket `i` (strictly increasing since
       `w[i] >= 1`).
    3. Sample uniformly: Pick a random integer `target` in
       `[1, total_sum]`, giving every bucket `i` exactly `w[i]` winning
       numbers out of `total_sum`.
    4. Binary search the bucket: Use `bisect_left` to find the smallest
       index `i` where `prefix_sums[i] >= target`.

Complexity:
    __init__: Time O(n), Space O(n)
    pickIndex: Time O(log n), Space O(1)
"""


import random


class Solution:
    def __init__(self, w: list[int]):
        self.prefix_sums = [0] * len(w)
        current_sum = 0
        for i, weight in enumerate(w):
            current_sum += weight
            self.prefix_sums[i] = current_sum
        self.total_sum = current_sum

    def pickIndex(self) -> int:
        target = random.randint(1, self.total_sum)
        left, right = 0, len(self.prefix_sums) - 1

        while left < right:
            mid = (left + right) // 2
            if self.prefix_sums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left
