"""
Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.
Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.

Example 1:
Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88. 

Note:
1 <= items.length <= 1000
items[i].length == 2
The IDs of the students is between 1 to 1000
The score of the students is between 1 to 100
For each student, there are at least 5 scores
"""


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = {}

        for item in items:
            if item[0] in scores:
                scores[item[0]].append(item[1])
            else:
                scores[item[0]] = [item[1]]

        res = []

        for i, score in scores.items():
            avg5 = sum(sorted(score, reverse=True)[:5]) // 5
            res.append([i, avg5])

        return res
