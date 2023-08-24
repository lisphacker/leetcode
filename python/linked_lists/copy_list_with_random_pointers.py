"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        
        i = head
        out = out2 = None
        prev = prev2 = None
        while i is not None:
            n = Node(i.val, None, i.random)
            n2 = Node(i.val, None, i)
            i.random = n
            
            if out is None:
                out = n
            if prev is not None:
                prev.next = n
            prev = n
            
            if out2 is None:
                out2 = n2
            if prev2 is not None:
                prev2.next = n2
            prev2 = n2
            
            i = i.next
            
        o = out
        o2 = out2
        while o is not None:
            r = o.random
            o2.random = r
            if r is None:
                o.random = None
            else:
                o.random = r.random
            o = o.next
            o2 = o2.next
            
        return out