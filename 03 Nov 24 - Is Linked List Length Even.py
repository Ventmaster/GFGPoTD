# 03rd November 2024
# Is Linked List Length Even?

class Solution:
    # your task is to complete this function
    # function should return false if length is even
    # else return true
    def isLengthEven(self, head):
        # Code here
        count = 1
        
        while head:
            if head.next is not None:
                count += 1
                
            head = head.next
            
        if count % 2 == 0:
            return True
            
        return False

