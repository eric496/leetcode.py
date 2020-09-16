"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.

Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""

"""
Thought process:
    1. If the two linked lists have intersection, then the intersection occurs from some node to the end of both linked lists.
    2. What we want is to let both linked lists to reach their tails simultaneously so we can check whether they have intersections in the latter parts of the lists.
    3. In order to achieve this, count the length of both lists, and let the longer one traverse the difference in the length number of nodes, which assures they will reach the end simultaneously.
    4. From there, let both lists traverse simultaneously. If there is same node, that is where the intersection occurs.   
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        n1 = n2 = 1
        cur1 = headA
        cur2 = headB
        
        while cur1:
            n1 += 1
            cur1 = cur1.next
            
        while cur2:
            n2 += 1 
            cur2 = cur2.next
            
        cur1 = headA
        cur2 = headB
        
        if n1 > n2:
            for _ in range(n1 - n2):
                cur1 = cur1.next
        else:
            for _ in range(n2 - n1):
                cur2 = cur2.next
                
        while cur1 and cur2:
            if cur1 is cur2:
                return cur1
            else:
                cur1 = cur1.next
                cur2 = cur2.next
                
        return None
