# 18 November 2023
# Reverse a Doubly Linked List

class Solution:
    def reverseDLL(self, head):
        #return head after reversing
        if head is None or head.next is None:
            return head
            
        temp = None
        current = head
        fwd = head
        
        while fwd:
            fwd = current.next
            current.next = temp
            current.prev = fwd
            temp = current
            current = fwd
            
        return temp
