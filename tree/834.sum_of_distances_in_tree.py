"""
An undirected, connected tree with N nodes labelled 0...N-1 and N-1 edges are given.
The ith edge connects nodes edges[i][0] and edges[i][1] together.
Return a list ans, where ans[i] is the sum of the distances between node i and all other nodes.

Example 1:
Input: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: 
Here is a diagram of the given tree:
  0
 / \
1   2
   /|\
  3 4 5
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.  Hence, answer[0] = 8, and so on.

Note: 1 <= N <= 10000
"""


from collections import defaultdict


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        sub = defaultdict(set)
        res = [0] * N
        cnt = [1] * N

        for u, v in edges:
            sub[u].add(v)
            sub[v].add(u)

        self.dfs1(0, -1, sub, res, cnt)
        self.dfs2(0, -1, N, sub, res, cnt)

        return res

    def dfs1(
        self, node: int, ancestor: int, sub: dict, res: List[int], cnt: List[int]
    ) -> None:
        for child in sub[node]:
            if child != ancestor:
                self.dfs1(child, node, sub, res, cnt)
                cnt[node] += cnt[child]
                res[node] += res[child] + cnt[child]

    def dfs2(
        self,
        node: int,
        ancestor: int,
        N: int,
        sub: dict,
        res: List[int],
        cnt: List[int],
    ) -> None:
        for child in sub[node]:
            if child != ancestor:
                res[child] = res[node] - cnt[child] + N - cnt[child]
                self.dfs2(child, node, N, sub, res, cnt)
