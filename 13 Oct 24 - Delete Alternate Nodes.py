# 13th October 2024
# Delete Alternate Nodes

class Solution:
    def deleteAlt(self, head):
        # code here
        while head and head.next:
            head.next = head.next.next
            head = head.next
            
        return head
