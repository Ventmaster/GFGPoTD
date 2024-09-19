# 19th September 2024
# Reverse Words

class Solution:
    #Function to reverse words in a given string.
    def reverseWords(self,str):
        # code here 
        return ".".join(str.split('.')[::-1])
