# 04 February 2024
# Subtraction in Linked List

class Node:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

class Solution:
    def subLinkedList(self, l1, l2): 
        # Code here
        # return head of difference list
        s1 = ""
        while l1:
            k = l1.data
            s1 += str(k)
            l1 = l1.next
            
        s2 = ""
        while l2:
            a = l2.data
            s2 += str(a)
            l2 = l2.next
            
        result = abs(int(s1) - int(s2))
        array_r = list(map(int, str(result)))
        head_r = Node(array_r[0])
        current = head_r
        
        for value in array_r[1:]:
            current.next = Node(value)
            current = current.next
            
        return head_r
