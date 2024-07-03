# 03 July 2024
# Remove all occurences of duplicates in a linked list

class Solution:
    def removeAllDuplicates(self, head):
        #code here
        temp = Node(-1)
        n = temp
        
        while head is not None:
            count = 1
            
            while head.next is not None and head.data == head.next.data:
                count += 1
                head = head.next
                
            if count == 1:
                new_node = Node(head.data)
                n.next = new_node
                n = n.next
            
            head = head.next
            
        return temp.next
