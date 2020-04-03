"""
Design a hit counter which counts the number of hits received in the past 5 minutes.
Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.
It is possible that several hits arrive roughly at the same time.

Example:
HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301); 

Follow up:
What if the number of hits per second could be very large? Does your design scale?
"""


# Solution: use a queue
from collections import deque


class HitCounter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.q.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.q and timestamp - self.q[0] >= 300:
            self.q.popleft()

        return len(self.q)


# Follow up: use a dictionary
class HitCounter:
    def __init__(self):
        self.cnt = {}

    def hit(self, timestamp: int) -> None:
        self.cnt[timestamp] = self.cnt.get(timestamp, 0) + 1

    def getHits(self, timestamp: int) -> int:
        res = 0

        for key in list(self.cnt.keys()):
            if timestamp - key >= 300:
                del self.cnt[key]
            else:
                res += self.cnt[key]

        return res
