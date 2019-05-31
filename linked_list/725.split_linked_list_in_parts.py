"""
Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".
The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.
The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.
Return a List of ListNode's representing the linked list parts that are formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]

Example 1:
Input: 
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but it's string representation as a ListNode is [].

Example 2:
Input: 
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.

Note:
The length of root will be in the range [0, 1000].
Each value of a node in the input will be an integer in the range [0, 999].
k will be an integer in the range [1, 50].
"""

"""
Thought process:
    Hint: If there are N nodes in the list, and k parts, then every part has N/k elements, except the first N%k parts have an extra one.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Solution 1
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        sentinel = walk = ListNode(None)
        sentinel.next = root
        n = 0
        
        while walk:
            walk = walk.next
            n += 1
        
        partitions = [n//k] * k
        
        for i in range(n%k-1):
            partitions[i] += 1
        
        walk = sentinel
        res = []
        
        for p in partitions:
            cur = []
            while p and walk.next:
                walk = walk.next
                cur.append(walk.val)
                p -= 1
            
            res.append(cur)
            
        return res


# Solution 2
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:        
        walk = root
        cnt = 0
        
        while walk:
            cnt += 1
            walk = walk.next
        
        chunk_size, num_longer_chunks = divmod(cnt, k)
        partitions = [chunk_size+1] * num_longer_chunks + [chunk_size] * (k-num_longer_chunks)
        res = [None] * k
        walk = root
        part_h = walk
        
        for i, part in enumerate(partitions):
            for j in range(part):
                if j == part-1:
                    res[i] = part_h
                    nxt = walk.next
                    walk.next = None
                    walk = nxt
                    part_h = nxt
                else:
                    walk = walk.next
        
        return res
        