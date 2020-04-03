"""
There are 8 prison cells in a row, and each cell is either occupied or vacant.
Each day, whether the cell is occupied or vacant changes according to the following rules:
If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)
We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.
Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

Example 1:
Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:
Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]

Note:
cells.length == 8
cells[i] is in {0, 1}
1 <= N <= 10^9
"""

# Brute force: TLE
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        for _ in range(N):
            new_state = [0] * len(cells)
            for i in range(1, len(cells) - 1):
                if cells[i - 1] == cells[i + 1]:
                    new_state[i] = 1
            cells = new_state

        return cells


# The first and last cells will inevitably become 0s.
# There are only 2^6 = 64 different states. Use hashmap to store all the states.
# Find the cycle and take mod
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        seen = set()
        cycle = has_cycle = 0

        for _ in range(N):
            new_state = self.next_state(cells)
            if tuple(new_state) in seen:
                has_cycle = 1
                break
            else:
                seen.add(tuple(new_state))
                cycle += 1

            cells = new_state

        if has_cycle:
            N %= cycle

            for _ in range(N):
                new_state = self.next_state(cells)
                cells = new_state

        return cells

    def next_state(self, cells: List[int]) -> List[int]:
        new_state = [0] * len(cells)

        for i in range(1, len(cells) - 1):
            new_state[i] = 1 if cells[i - 1] == cells[i + 1] else 0

        return new_state
