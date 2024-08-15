# 16th August 2024
# Add 1 to a Linked List Number

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    def addOne(self,head):
        #Returns new head of linked List.
        num = 0 
        
        while head:
            num, head = num*10+head.data, head.next
            
        return Node(num+1)
