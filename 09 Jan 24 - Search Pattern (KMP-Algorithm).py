# 09 January 2024
# Search Pattern (KMP-Algorithm)

class Solution:
    def search(self, pat, txt):
        # code here
        indexes = []
        starting_index = 0
        
        while starting_index < len(txt):
            x = txt.find(pat, starting_index)
            
            if x == -1:
                break
            indexes.append(x+1)
            starting_index = x + 1
            
        return indexes
