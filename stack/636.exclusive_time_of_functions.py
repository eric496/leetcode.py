"""
On a single threaded CPU, we execute some functions.  Each function has a unique id between 0 and N-1.
We store logs in timestamp order that describe when a function is entered or exited.
Each log is a string with this format: "{function_id}:{"start" | "end"}:{timestamp}".  For example, "0:start:3" means the function with id 0 started at the beginning of timestamp 3.  "1:end:2" means the function with id 1 ended at the end of timestamp 2.
A function's exclusive time is the number of units of time spent in this function.  Note that this does not include any recursive calls to child functions.
The CPU is single threaded which means that only one function is being executed at a given time unit.
Return the exclusive time of each function, sorted by their function id.

Example 1:
Input:
n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
Output: [3, 4]
Explanation:
Function 0 starts at the beginning of time 0, then it executes 2 units of time and reaches the end of time 1.
Now function 1 starts at the beginning of time 2, executes 4 units of time and ends at time 5.
Function 0 is running again at the beginning of time 6, and also ends at the end of time 6, thus executing for 1 unit of time. 
So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time executing.

Note:
1 <= n <= 100
Two functions won't start or end at the same time.
Functions will always log when they exit.
"""

"""
Thought Process:
    1. Model the CPU call stack: Maintain `stack` holding active function IDs,
       where `stack[-1]` is the function currently holding the CPU, and
       `prev_time` marking when the current execution slice began.
    2. Handle "start" logs (beginning of `timestamp`):
       - If `stack` is non-empty, credit `timestamp - prev_time` units to the
         paused caller `stack[-1]`.
       - Push `func_id` onto `stack` and set `prev_time = timestamp`.
    3. Handle "end" logs (end of `timestamp`):
       - Pop the finishing function `stack.pop()` and credit
         `timestamp - prev_time + 1` units (inclusive of `timestamp`).
       - Advance `prev_time = timestamp + 1` because the caller resumes at
         the start of the next time unit.

Complexity:
    Time: O(m) — single linear pass over `m = len(logs)`.
    Space: O(m) — worst-case call stack depth when calls are deeply nested.

"""


class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        stack = []
        res = [0] * n
        prev_time = 0

        for log in logs:
            func_id_str, event, timestamp_str = log.split(":")
            func_id = int(func_id_str)
            timestamp = int(timestamp_str)

            if event == "start":
                if stack:
                    res[stack[-1]] += timestamp - prev_time
                stack.append(func_id)
                prev_time = timestamp
            else:
                res[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1
        
        return res
