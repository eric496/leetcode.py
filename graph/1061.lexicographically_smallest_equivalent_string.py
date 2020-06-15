"""
Given strings A and B of the same length, we say A[i] and B[i] are equivalent characters. For example, if A = "abc" and B = "cde", then we have 'a' == 'c', 'b' == 'd', 'c' == 'e'.
Equivalent characters follow the usual rules of any equivalence relation:
Reflexivity: 'a' == 'a'
Symmetry: 'a' == 'b' implies 'b' == 'a'
Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'
For example, given the equivalency information from A and B above, S = "eed", "acd", and "aab" are equivalent strings, and "aab" is the lexicographically smallest equivalent string of S.
Return the lexicographically smallest equivalent string of S by using the equivalency information from A and B.

Example 1:
Input: A = "parker", B = "morris", S = "parser"
Output: "makkek"
Explanation: Based on the equivalency information in A and B, we can group their characters as [m,p], [a,o], [k,r,s], [e,i]. The characters in each group are equivalent and sorted in lexicographical order. So the answer is "makkek".

Example 2:
Input: A = "hello", B = "world", S = "hold"
Output: "hdld"
Explanation:  Based on the equivalency information in A and B, we can group their characters as [h,w], [d,e,o], [l,r]. So only the second letter 'o' in S is changed to 'd', the answer is "hdld".

Example 3:
Input: A = "leetcode", B = "programs", S = "sourcecode"
Output: "aauaaaaada"
Explanation:  We group the equivalent characters in A and B as [a,o,e,r,s,c], [l,p], [g,t] and [d,m], thus all letters in S except 'u' and 'd' are transformed to 'a', the answer is "aauaaaaada".

Note:
String A, B and S consist of only lowercase English letters from 'a' - 'z'.
The lengths of string A, B and S are between 1 and 1000.
String A and B are of the same length.
"""


class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        parent = list(range(26))

        for a, b in zip(A, B):
            self.union(ord(a) - ord("a"), ord(b) - ord("a"), parent)

        res = []

        for c in S:
            res.append(chr(self.find(ord(c) - ord("a"), parent) + ord("a")))

        return "".join(res)

    def find(self, u: int, parent: List[int]) -> int:
        if u == parent[u]:
            return u

        root = self.find(parent[u], parent)
        parent[u] = root
        return root

    def union(self, u: int, v: int, parent: List[int]) -> None:
        u_root = self.find(u, parent)
        v_root = self.find(v, parent)

        if u_root == v_root:
            return

        if u_root > v_root:
            parent[u_root] = v_root
        else:
            parent[v_root] = u_root
