# 09 March 2024
# Find the N-th character

class Solution:
    def nthCharacter(self, s, r, n):
        # code here
        temporary = s
        
        for i in range(r):
            temporary = ''.join("01" if temporary[i] == '0' else "10" for i in range((n//2)+1))
            
        return temporary[n]
