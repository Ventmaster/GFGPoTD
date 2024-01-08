# 08 January 2024
# Merge 2 sorted linked list in reverse order

class Solution:
    def mergeResult(self, h1, h2):
        #return head of merged list
        li = []
        current = h1
        new_current = h2
        
        while (current):
            li.append(current.data)
            current = current.next
        
        while (new_current):
            li.append(new_current.data)
            new_current = new_current.next
        
        li.sort()
        li = li[::-1]
        
        dummy = Node(0)
        result = dummy
        
        for i in li:
            result.next = Node(i)
            result = result.next
        
        return dummy.next
