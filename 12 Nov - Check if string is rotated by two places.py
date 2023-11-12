# 12 November 2023
# Check if string is rotated by two places

class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,str1,str2):
        #code here
        if str1[2:] + str1[:2] == str2 or str1[len(str1)-2:] + str1[:len(str1)-2] == str2:
            return 1
        else:
            return 0
