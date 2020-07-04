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


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        if not cells or N <= 0:
            return cells
        
        has_cycle = False
        days = 0
        states = set()
        cur = cells
        
        for _ in range(N):
            nxt = self.next_day(cur)
            cur_state = "".join(map(str, nxt))
            
            if cur_state not in states:
                states.add(cur_state)
                days += 1
            else:
                has_cycle = True
                break
            
            cur = nxt
        
        if has_cycle:
            N %= days
            
            for _ in range(N):
                cur = self.next_day(cur)
                
        return cur
    
    def next_day(self, cells: List[int]) -> List[int]:
        res = [0] * len(cells)
        
        for i in range(1, len(cells) - 1):
            res[i] = 1 if cells[i-1] == cells[i+1] else 0
            
        return res
    