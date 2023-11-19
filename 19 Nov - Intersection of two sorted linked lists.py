# 19 November 2023
# Intersection of two sorted linked lists

from collections import defaultdict

class Solution:
    def findIntersection(self,head1,head2):
        #return head
        dic = defaultdict(int)
        curr1 = head1
        
        while curr1:
            dic[curr1.data] += 1
            curr1 = curr1.next
        # for i in dic:
        #     print(i)
        
        temp= None
        newHead = None
        prevNode = None
        curr2 = head2
        
        while curr2:
            if curr2.data in dic:
                dic[curr2.data] -= 1
                if dic[curr2.data] == 0:
                    del dic[curr2.data]
                
                temp = Node(curr2.data)
                if newHead== None: 
                    newHead = temp
                else:
                    prevNode.next = temp
                
                #change the position of prevNode
                prevNode = temp
            curr2= curr2.next
        
        return newHead
