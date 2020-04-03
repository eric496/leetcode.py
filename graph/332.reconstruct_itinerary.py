"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.

Example 1:
Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:
Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""


from collections import deque


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        targets = {}

        for depart, arrival in sorted(tickets):
            if depart in targets:
                targets[depart].append(arrival)
            else:
                targets[depart] = deque([arrival])

        route = []
        self.visit("JFK", targets, route)

        return route[::-1]

    def visit(self, airport: str, targets: dict, route: List) -> None:
        while airport in targets and targets[airport]:
            self.visit(targets[airport].popleft(), targets, route)

        route.append(airport)
