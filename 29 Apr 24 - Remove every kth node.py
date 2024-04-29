# 29 April 2024
# Remove every kth node

class Solution:
    def deleteK(self, head, k):
        #code here  
        current = head
        previous = None
        i = 1
        
        if k == 1:
            return None
            
        while current:
            if i == k:
                i = 1
                
                if current == head:
                    current = head.next
                    head = None
                    head = current
                    
                if previous:
                    previous.next = current.next
                    
            else:
                i = i + 1
                
            previous = current
            current = current.next
            
        return head
