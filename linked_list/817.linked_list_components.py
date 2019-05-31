"""
We are given head, the head node of a linked list containing unique integer values.
We are also given the list G, a subset of the values in the linked list.
Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.

Example 1:
Input: 
head: 0->1->2->3
G = [0, 1, 3]
Output: 2
Explanation: 
0 and 1 are connected, so [0, 1] and [3] are the two connected components.

Example 2:
Input: 
head: 0->1->2->3->4
G = [0, 3, 1, 4]
Output: 2
Explanation: 
0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.

Note:
If N is the length of the linked list given by head, 1 <= N <= 10000.
The value of each node in the linked list will be in the range [0, N - 1].
1 <= G.length <= 10000.
G is a subset of all values in the linked list.
"""

"""
Thought process:
    Traverse the linked list, check if the current node value is in the set. If so, start a counter and keep counting till the end of the component.
    Increment result by 1 when component ends, and clear up the counter.
    IMPORTANT: If the counter has non-zero value after the loop, result should be incremented by 1, because the last component in the list is not counted in the loop.
"""

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        set_G = set(G)
        res = cnt = 0
        
        while head:
            if head.val in set_G:
                cnt += 1
            else:
                res += 1 if cnt else 0
                cnt = 0
            head = head.next
            
        return res+1 if cnt else res
