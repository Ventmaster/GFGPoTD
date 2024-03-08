# 08 March 2024
# Check if frequencies can be equal

class Solution:
    def sameFreq(self, s):
        # code here
        new_set = set(s)
        dic = {}
        
        for i in new_set:
            dic[i] = s.count(i)
            
        frequency_count = {}
        
        for count in dic.values():
            if count in frequency_count:
                frequency_count[count] += 1
            else:
                frequency_count[count] = 1
                
        if len(frequency_count) == 1:
            return True
            
        if len(frequency_count) == 2:
            maximum_frequency = max(frequency_count.keys())
            minimum_frequency = min(frequency_count.keys())
            
            if (minimum_frequency == 1 and frequency_count[minimum_frequency] == 1) or (maximum_frequency - minimum_frequency == 1 and frequency_count[maximum_frequency] == 1):
                return True
        
        return False
