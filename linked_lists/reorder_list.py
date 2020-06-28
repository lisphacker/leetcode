# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def print(self, head, name, maxn = 10000):
        print(name,)
        h = head
        i = 0
        while h is not None and i < maxn:
            print(h.val,)
            h = h.next
            i += 1
        print('')
        
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if head is None:
            return
        
        n = 0
        h = head
        while h is not None:
            n += 1
            h = h.next
            
        n2 = n // 2
        
        h = head
        for i in range(n2):
            h = h.next
            
        p = h
        h = h.next
        
        while h is not None:
            n = h.next
            h.next = p
            p = h
            h = n
            
        tail = p
        
        h = head
        t = tail
        
        self.print(head, 'HEAD', 6)
        self.print(tail, 'TAIL', 6)
        
        for i in range(n2):
            n = h.next
            h.next = t
            n2 = t.next
            t.next = n
            h = n
            t = n2
            
        h.next = None
            
        self.print(head, 'OUT', 6)
        
        