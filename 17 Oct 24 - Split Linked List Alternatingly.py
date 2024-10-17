# 17th October 2024
# Split Linked List Alternatingly

class Solution:
    def alternatingSplitList(self, head):
        #Your code here
        count = 0
        head1, head2 = None, None
        c1, c2 = None, None
        
        while head:
            if count == 0:
                head1 = c1 = Node(head.data)
            elif count == 1:
                head2 = c2 = Node(head.data)
            
            elif count % 2 == 0:
                temp = Node(head.data)
                c1.next = temp
                c1 = c1.next
                
            elif count % 2 != 0:
                temp = Node(head.data)
                c2.next = temp
                c2 = c2.next
                
            head = head.next
            count += 1
            
        return [head1, head2]
