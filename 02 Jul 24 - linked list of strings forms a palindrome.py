# 02 July 2024
# linked list of strings forms a palindrome

def palindrome(s):
    return s == s[::-1]

def compute(head): 
    #return True/False
    s = ""
    
    while head:
        s += head.data
        head = head.next
        
    result = palindrome(s)
    
    return True if result else False
