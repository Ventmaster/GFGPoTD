# 21st September 2024
# Clone a linked list with next and random pointer

class Solution:
    #Function to clone a linked list with next and random pointer.
    def copyList(self, head):
        # code here
        d = dict()
        
        temp = head
        while temp:
            d[temp] = Node(temp.data)
            temp = temp.next
        
        d[None] = None
        temp = head
        while temp:
            d[temp].next = d[temp.next]
            d[temp].random = d[temp.random]
            temp = temp.next
        
        return d[head]
