"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Constraints:
2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
"""


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2 and coordinates[0] != coordinates[1]:
            return True
        
        x, y = coordinates[0][0]-coordinates[1][0], coordinates[0][1]-coordinates[1][1]
        slope = y / x if x else float('inf')
        
        for i in range(1, len(coordinates)-1):
            x, y = coordinates[i][0] - coordinates[i+1][0], coordinates[i][1] - coordinates[i+1][1]
            alpha = y / x if x else float('inf') 
            if alpha != slope:
                return False
            
        return True


# Improved: using multiplication to replace division
# So you don't have handle the zero division issue
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        
        for i in range(len(coordinates)-1):
            x2, y2 = coordinates[i]
            x3, y3 = coordinates[i+1]
            if (y1-y0) * (x3-x2) != (x1-x0) * (y3-y2):
                return False
            
        return True