# 25th September 2024
# Palindrome Linked List

class Solution:
    def isPalindrome(self, head):
        #code here
        flatten = []
        temp = head
        
        while temp:
            flatten.append(temp.data)
            temp = temp.next
            
        n = len(flatten)
        
        return flatten[:n//2] == flatten[(n+1)//2:][::-1]
