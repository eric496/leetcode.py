"""
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.
According to the example above:
equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
"""


# Solution 1: Union Find
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        res = []
        parent = {}
        weight = {}
        
        for u, v in equations:
            parent[u] = u
            weight[u] = 1.0
            parent[v] = v
            weight[v] = 1.0
            
        for i, (u, v) in enumerate(equations):
            self.union(u, v, parent, weight, values[i])
            
        for u, v in queries:
            if u not in parent or v not in parent:
                res.append(-1.0)
                continue
                
            u_root = self.find(u, parent, weight)
            v_root = self.find(v, parent, weight)
            
            if u_root != v_root:
                res.append(-1.0)
                continue
            
            res.append(weight[u] / weight[v])

        return res
        
    def find(self, u: str, parent: dict, weight: dict) -> str:
        if u == parent[u]:
            return u
        else:
            root = self.find(parent[u], parent, weight)
            p = parent[u]
            parent[u] = root
            weight[u] = weight[u] * weight[p]
            return root
        
    def union(self, u: str, v: str, parent: dict, weight: dict, val: float) -> None:
        u_root = self.find(u, parent, weight)
        v_root = self.find(v, parent, weight)
        parent[u_root] = v_root
        weight[u_root] = weight[v] * val / weight[u]
    