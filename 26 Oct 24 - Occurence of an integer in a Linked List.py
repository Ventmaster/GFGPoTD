# 26th October 2024
# Occurence of an integer in a Linked List

class Solution:
    def count(self, head, key):
        # Code here
        result = 0
        
        while head:
            if head.data == key:
                result += 1
                
            head = head.next
            
        return result
