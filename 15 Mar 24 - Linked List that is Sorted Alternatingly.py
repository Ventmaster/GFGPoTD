# 15 March 2024
# Linked List that is Sorted Alternatingly

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Solution:
    def sort(self, h1):
        #return head
        array = []
        new = h1
        
        while new:
            array.append(new.data)
            new = new.next
            
        x = sorted(array)
        
        for i in range(len(x)):
            print(x[i], end = " ")
