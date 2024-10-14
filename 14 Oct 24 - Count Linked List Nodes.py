# 14th October 2024
# Count Linked List Nodes

class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        # code here
        length = 0
        
        while head:
            length += 1
            head = head.next
            
        return length
