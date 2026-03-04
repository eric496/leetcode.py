"""
In a forest, each rabbit has some color. Some subset of rabbits (possibly all of them) tell you how many other rabbits have the same color as them. Those answers are placed in an array.
Return the minimum number of rabbits that could be in the forest.

Examples:
Input: answers = [1, 1, 2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit than answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

Input: answers = [10, 10, 10]
Output: 11

Input: answers = []
Output: 0

Note:
answers will have length at most 1000.
Each answers[i] will be an integer in the range [0, 999].
"""


# Solution 1 - Greedy
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()

        i = 0
        n = len(answers)
        rabbits = 0

        while i < n:
            rabbits += answers[i] + 1
            limit = answers[i]
            i += 1
            
            while limit > 0 and i < n and answers[i] == answers[i-1]:
                i += 1
                limit -= 1

        return rabbits


# Solution 2 - hash table
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        if not answers:
            return 0

        cnt, res = {}, 0

        for answer in answers:
            if answer == 0:
                res += 1
                continue

            if answer in cnt:
                cnt[answer] += 1
                if cnt[answer] == answer:
                    del cnt[answer]
            else:
                cnt[answer] = 0
                res += answer + 1

        return res
    
    
    # Solution 3 - math
    class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = defaultdict(int)
        for answer in answers:
            counts[answer] += 1
        
        rabbits = 0

        for k, v in counts.items():
            groups = (v + k) // (k + 1)
            rabbits += groups * (k + 1)

        return rabbits
