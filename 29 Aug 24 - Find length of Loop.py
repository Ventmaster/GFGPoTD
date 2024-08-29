# 29th August 2024
# Find length of Loop

class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        #Your code here
        x = {}
        count = 0
        
        while head:
            count += 1
            
            if head in x:
                return count - x[head]
                
            x[head] = count
            head = head.next
            
        return 0
