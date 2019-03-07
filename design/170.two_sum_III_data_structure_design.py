'''
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false
Example 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false
'''

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.d[number] = self.d.get(number, 0) + 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for k in self.d:
            if value-k in self.d:
                # A corner case: add(0), find(0)
                if value-k == k:
                    if self.d[k] > 1:
                        return True
                    # No else statement to return false because add(-1), add(1), find(0)
                else:
                    return True
            
        return False