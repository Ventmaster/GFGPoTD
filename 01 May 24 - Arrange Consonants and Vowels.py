# 01 May 2024
# Arrange Consonants and Vowels

class Solution:
    #Function to reverse a linked list.
    def arrangeCV(self, head):
        # Code here
        vowels = ['a', 'e', 'i', 'o', 'u']
        current = head
        V, C = [], []
        n = 0
        
        while current:
            if current.data in vowels:
                V.append(current.data)
            else:
                C.append(current.data)
                
            n += 1
            
            current = current.next
            
        LL = Linked_List()
        
        for i in V:
            LL.insert(i)
        for i in C:
            LL.insert(i)
            
        return LL.head
