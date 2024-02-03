# 03 February 2024
# Decimal Equivalent of Binary Linked List

class Solution:
    def decimalValue(self, head):
        MOD=10**9+7
        # Code here
        val = 0
        
        while head:
            val = (val * 2 + head.data) % MOD
            head = head.next
            
        return val
