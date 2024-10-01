# 01st October 2024
# Multiply two linked lists

class Solution:
    def multiply_two_lists(self, first, second):
        # Code here
        fir, sec = 0, 0
        current = first
        current_ = second
        
        while (current):
            fir = (current.data + (fir * 10))
            current = current.next
            
        while (current_):
            sec = (current_.data + (sec * 10))
            current_ = current_.next
            
        result = (fir * sec) % 1000000007
        
        return result
