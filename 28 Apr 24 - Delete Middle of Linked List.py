# 28 April 2024
# Delete Middle of Linked List

class Solution:
    def deleteMid(self,head):
        '''
        head:  head of given linkedList
        return: head of resultant llist
        '''
        #code here
        if head == None or head.next == None:
            return None
            
        slow = head
        fast = head
        temporary = head
        
        while fast and fast.next:
            temporary = slow
            slow = slow.next
            fast = fast.next.next
            
        temporary.next = slow.next
        
        return head
