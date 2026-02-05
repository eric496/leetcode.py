"""
There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).
You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.
Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

Example 1:
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false

Example 2:
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true

Constraints:
    1 <= trips.length <= 1000
    trips[i].length == 3
    1 <= numPassengersi <= 100
    0 <= fromi < toi <= 1000
    1 <= capacity <= 105
"""


# Solution 1: heap
import heapq


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        load = 0
        heap = []

        for num, start, end in trips:
            while heap and heap[0][0] <= start:
                _, offs = heapq.heappop(heap)
                load -= offs
            
            load += num

            if load > capacity:
                return False

            heapq.heappush(heap, (end, num))

        return True


# Solution 2: sweep line
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []

        for num, start, end in trips:
            events.append((start, num))
            events.append((end, -num))

        events.sort()
        
        load = 0
        for loc, num in events:
            load += num

            if load > capacity:
                return False

        return True
    