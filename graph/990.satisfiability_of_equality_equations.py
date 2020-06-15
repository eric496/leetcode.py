"""
Given an array equations of strings that represent relationships between variables, each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.
Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.

Example 1:
Input: ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.

Example 2:
Input: ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

Example 3:
Input: ["a==b","b==c","a==c"]
Output: true

Example 4:
Input: ["a==b","b!=c","c==a"]
Output: false

Example 5:
Input: ["c==c","b==d","x!=z"]
Output: true

Note:
1 <= equations.length <= 500
equations[i].length == 4
equations[i][0] and equations[i][3] are lowercase letters
equations[i][1] is either '=' or '!'
equations[i][2] is '='
"""


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        eq = [[e[0], e[-1]] for e in equations if e[1] == "="]
        neq = [[e[0], e[-1]] for e in equations if e[1] == "!"]
        parent = list(range(26))
        rank = [0] * 26

        for u, v in eq:
            self.union(ord(u) - ord("a"), ord(v) - ord("a"), parent, rank)

        for u, v in neq:
            if self.find(ord(u) - ord("a"), parent) == self.find(
                ord(v) - ord("a"), parent
            ):
                return False

        return True

    def find(self, u: int, parent: List[int]) -> int:
        return u if u == parent[u] else self.find(parent[u], parent)

    def union(self, u: int, v: int, parent: List[int], rank: List[int]) -> None:
        u_root = self.find(u, parent)
        v_root = self.find(v, parent)

        if u_root == v_root:
            return

        if rank[u_root] > rank[v_root]:
            parent[v_root] = u_root
        elif rank[u_root] < rank[v_root]:
            parent[u_root] = v_root
        else:
            parent[v_root] = u_root
            rank[u_root] += 1
