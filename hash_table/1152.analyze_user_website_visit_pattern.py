"""
We are given some website visits: the user with name username[i] visited the website website[i] at time timestamp[i].
A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits.  (The websites in a 3-sequence are not necessarily distinct.)
Find the 3-sequence visited by the largest number of users. If there is more than one solution, return the lexicographically smallest such 3-sequence.

Example 1:
Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]
Explanation: 
The tuples in this example are:
["joe", 1, "home"]
["joe", 2, "about"]
["joe", 3, "career"]
["james", 4, "home"]
["james", 5, "cart"]
["james", 6, "maps"]
["james", 7, "home"]
["mary", 8, "home"]
["mary", 9, "about"]
["mary", 10, "career"]
The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.

Note:
3 <= N = username.length = timestamp.length = website.length <= 50
1 <= username[i].length <= 10
0 <= timestamp[i] <= 10^9
1 <= website[i].length <= 10
Both username[i] and website[i] contain only lowercase characters.
It is guaranteed that there is at least one user who visited at least 3 websites.
No user visits two websites at the same time.
"""


class Solution:
    def mostVisitedPattern(
        self, username: List[str], timestamp: List[int], website: List[str]
    ) -> List[str]:
        seq = sorted(list(zip(username, timestamp, website)))
        page_visit_by_user = {name: [] for name in set(username)}

        for username, timestamp, website in seq:
            page_visit_by_user[username].append(website)

        page_visit_sequence_count = {}

        for pages in page_visit_by_user.values():
            if len(pages) >= 3:
                seen_seq = set()
                for i in range(len(pages) - 2):
                    for j in range(i + 1, len(pages) - 1):
                        for k in range(j + 1, len(pages)):
                            seq3 = pages[i], pages[j], pages[k]
                            if seq3 not in seen_seq:
                                page_visit_sequence_count[seq3] = (
                                    page_visit_sequence_count.get(seq3, 0) + 1
                                )
                            seen_seq.add(seq3)

        res, max_ = [], 0

        for k, v in page_visit_sequence_count.items():
            if v > max_:
                res = [k]
                max_ = v
            elif v == max_:
                res.append(k)

        return sorted(res)[0]
