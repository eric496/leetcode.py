"""
We have jobs: difficulty[i] is the difficulty of the ith job, and profit[i] is the profit of the ith job. 
Now we have some workers. worker[i] is the ability of the ith worker, which means that this worker can only complete a job with difficulty at most worker[i]. 
Every worker can be assigned at most one job, but one job can be completed multiple times.
For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.  If a worker cannot complete any job, his profit is $0.
What is the most profit we can make?

Example 1:
Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100 
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get profit of [20,20,30,30] seperately.

Notes:
1 <= difficulty.length = profit.length <= 10000
1 <= worker.length <= 10000
difficulty[i], profit[i], worker[i]  are in range [1, 10^5]
"""


# Solution 1: binary search
from collections import defaultdict


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        cur_max = float("-inf")
        aux = [(d, p) for d, p in zip(difficulty, profit)]
        aux.sort()
        difficulty.sort()
        mp = defaultdict(int)

        for d, p in aux:
            cur_max = max(cur_max, p)
            if d in mp:
                if cur_max > mp[d]:
                    mp[d] = cur_max
            else:
                mp[d] = cur_max

        res = 0

        for w in worker:
            print(self.lower_bound(difficulty, w))
            res += mp[self.lower_bound(difficulty, w)]

        return res

    def lower_bound(self, difficulty: List[int], target: int) -> int:
        if target < difficulty[0]:
            return 0
        elif target > difficulty[-1]:
            return difficulty[-1]

        lo, hi = 0, len(difficulty)

        while lo < hi:
            mid = lo + (hi - lo >> 1)

            if difficulty[mid] >= target:
                hi = mid
            else:
                lo = mid + 1

        return difficulty[lo] if difficulty[lo] <= target else difficulty[lo - 1]


# Solution 2: two pointers
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        res = i = best = 0
        n = len(jobs)
        
        for w in worker:
            while i < n and w >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i += 1
                
            res += best
        
        return res
