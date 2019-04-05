"""
Design a HashMap without using any built-in hash table libraries.
To be specific, your design should include these functions:
put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:
MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 

Note:
All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.
"""

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 10000
        self.map = [None] * self.capacity

        
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        ix = key % self.capacity
        
        if not self.map[ix]:
            self.map[ix] = ListNode(key, value)
        else:
            node = self.map[ix]
                
            while node:
                if node.key == key:
                    node.val = value
                    return
                
                if not node.next:
                    break
                
                node = node.next
            
            node.next = ListNode(key, value)
                

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        ix = key % self.capacity
        node = self.map[ix]

        while node:
            if node.key == key:
                return node.val

            node = node.next
            
        return -1

        
    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        ix = key % self.capacity
        
        if self.map[ix]:
            node = self.map[ix]
            
            if node.key == key:
                self.map[ix] = node.next
                return
             
            while node.next:
                if node.next.key == key:
                    node.next = node.next.next
                    break
                    
                node = node.next
