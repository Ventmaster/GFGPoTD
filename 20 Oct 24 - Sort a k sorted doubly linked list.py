# 20th October 2024
# Sort a k sorted doubly linked list

import heapq

class Solution:
    def sortAKSortedDLL(self, head, k):
        # Code Here
        p = q = head
        li = []
        
        while q:
            heapq.heappush(li, q.data)
            
            if len(li) >= k + 1:
                p.data = heapq.heappop(li)
                p = p.next
                
            q = q.next
            
        while li:
            p.data = heapq.heappop(li)
            p = p.next
            
        return head
