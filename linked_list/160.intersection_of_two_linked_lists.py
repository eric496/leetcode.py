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

'''
Thought process:
    1. If the two linked lists have intersection, then the intersection occurs from some node to the end of both linked lists.
    2. What we want is to let both linked lists to reach their tails simultaneously so we can check whether they have intersections in the latter parts of the lists.
    3. In order to achieve this, count the length of both lists, and let the longer one traverse the difference in the length number of nodes, which assures they will reach the end simultaneously.
    4. From there, let both lists traverse simultaneously. If there is same node, that is where the intersection occurs.   
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def getIntersectionNode(self, h1, h2):
        walk1, walk2 = h1, h2
        len1 = len2 = 0
        
        while walk1:
            walk1 = walk1.next
            len1 += 1
        
        while walk2:
            walk2 = walk2.next
            len2 += 1
            
        diff = abs(len1-len2)
        walk1, walk2 = h1, h2
 
        if len1 > len2:
            while diff:
                walk1 = walk1.next
                diff -= 1
                
        if len2 > len1:
            while diff:
                walk2 = walk2.next
                diff -= 1
        
        while walk1 and walk2:
            if walk1 is walk2:
                return walk1
            else:
                walk1, walk2 = walk1.next, walk2.next
        
        return None