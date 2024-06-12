# 12th June 2024
# Count numbers containing 4

class Solution:
    def countNumberswith4(self, n : int) -> int:
        # code here
        def check_for_four(num):
            while num:
                if num % 10 == 4:
                    return 1
                num //= 10
                
            return 0
            
        result = 0
        
        for i in range(1, n+1):
            result += check_for_four(i)
            
        return result
