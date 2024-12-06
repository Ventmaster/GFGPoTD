# 06th December 2024
# Find H-Index

class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        #code here
        n = len(citations)
        citations.sort(reverse = True)
        
        for i in range(n):
            if citations[i] < i + 1:
                return i
                
        return n
