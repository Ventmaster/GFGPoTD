# 10th August 2024
# Rotate a Linked List

class Solution:
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        temp = head
        li = []
        li1 = []
        
        while temp is not None:
            li.append(temp.data)
            temp = temp.next
            
        for i in range(k, len(li)):
            li1.append(li[i])
        
        li1.extend(li)
        
        new_k = len(li)
        new_li = Node(li1[0])
        head1 = new_li
        j = 0
        
        while j < new_k:
            new_li.next = Node(li1[j])
            new_li = new_li.next    
            j += 1
        
        return head1.next
