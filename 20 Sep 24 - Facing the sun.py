# 20th September 2024
# Facing the Sun

class Solution:
    # Returns count buildings that can see sunlight
    def countBuildings(self, height):
        # code here
        count = 0
        current_maximum = 0
        
        for i in height:
            if i > current_maximum:
                count += 1
                
            current_maximum = max(i, current_maximum)
            
        return count
