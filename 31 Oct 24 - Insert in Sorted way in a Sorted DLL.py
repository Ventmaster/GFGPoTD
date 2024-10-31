# 31st October 2024
# Insert in Sorted way in a Sorted DLL

class Solution:
    #Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
        #code here
        newnode = Node(x)
        
        if newnode.data <= head.data:
            newnode.next = head
            head = newnode
            
            return head
            
        current = head
        
        while current.next != None and current.next.data <= x:
            current = current.next
            
        if current.next == None:
            current.next = newnode
        else:
            newnode.next = current.next
            current.next = newnode
            
        return head
