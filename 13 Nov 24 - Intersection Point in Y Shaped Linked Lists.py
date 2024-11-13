# 13th November 2024
# Intersection Point in Y Shaped Linked Lists

def intersetPoint(head1,head2):
    #code here
    def func_for_getting_length(head):
        current = head
        length = 0
        
        while current:
            length += 1
            current = current.next
        
        return length
        
    len1 = func_for_getting_length(head1)
    len2 = func_for_getting_length(head2)
    
    current1 = head1
    current2 = head2 
    
    if len1 > len2:
        for _ in range(len1 - len2):
            current1 = current1.next
    else:
        for _ in range(len2 - len1):
            current2 = current2.next
            
    while current1 and current2:
        if current1 == current2:
            return current1.data
        
        current1 = current1.next
        current2 = current2.next
        
    return -1
