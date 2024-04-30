# 30 April 2024
# Add two numbers represented by linked lists

class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, num1, num2):
        # code here
        # return head of sum list
        n1, n2 = num1, num2
        x, y = "", ""
        
        while n1:
            x += str(n1.data)
            n1 = n1.next
        
        while n2:
            y += str(n2.data)
            n2 = n2.next
            
        ix, iy = int(x), int(y)
        
        result = ix + iy
        LL = LinkedList()
        answer = []
        
        if result == 0:
            answer = [0]
        
        while result > 0:
            answer.append(result % 10)
            result //= 10
            
        answer = answer[::-1]
        
        for i in answer:
            LL.insert(i)
            
        return LL.head
