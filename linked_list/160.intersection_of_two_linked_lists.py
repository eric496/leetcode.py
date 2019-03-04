'''
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
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution One: keep track of the head
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ptA, ptB = ListNode(-1), ListNode(-1)
        ptA.next, ptB.next = headA, headB
        cntA = cntB = 0 
        
        while ptA:
            cntA += 1
            ptA = ptA.next
        
        while ptB:
            cntB += 1
            ptB = ptB.next
            
        if cntA > cntB:
            diff = cntA - cntB
            longer, shorter = headA, headB
        else:
            diff = cntB - cntA
            longer, shorter = headB, headA
        
        ptL, ptS = ListNode(-1), ListNode(-1)
        ptL.next, ptS.next = longer, shorter
        
        while diff:
            ptL = ptL.next
            diff -= 1
        
        while ptL and ptS:
            if ptL == ptS:
                return ptL
            else:
                ptL = ptL.next
                ptS = ptS.next
        
        return None

# Solution Two: do not keep track of the head
class Solution(object):
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA, curB = headA, headB
        lenA = lenB = 0

        while curA:
            curA = curA.next
            lenA += 1
        while curB:
            curB = curB.next
            lenB += 1
        
        curA, curB = headA, headB
        
        if lenA > lenB:
            for _ in range(lenA-lenB):
                curA = curA.next
        else:
            for _ in range(lenB-lenA):
                curB = curB.next
        
        while curA and curB:
            if curA is curB:
                return curA
            else:
                curA, curB = curA.next, curB.next
        
        return None