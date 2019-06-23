"""
In a string S of lowercase letters, these letters form consecutive groups of the same character.
For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".
Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.
The final answer should be in lexicographic order.

Example 1:
Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.

Example 2:
Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.

Example 3:
Input: "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]

Note:  1 <= S.length <= 1000
"""


# Solution 1
class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        if len(S) < 3:
            return []

        start, end = 0, 1
        res = []

        while end < len(S):
            if S[end] == S[end-1]:
                end += 1
            else:
                if end-start >= 3:
                    res.append([start, end-1])
                start = end
                end += 1

        if end-start >= 3:
            res.append([start, end-1])

        return res


# Solution 2: more concise 
class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        start = end = 0
        res = []

        while start < len(S):
            while end < len(S):
                if S[start] == S[end]:
                    end += 1
                else:
                    break

            if end-start >= 3:
                res.append([start, end-1])

            start = end

        return res

