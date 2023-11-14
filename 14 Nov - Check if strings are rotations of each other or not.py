# 14 November 2023
# Check if strings are rotations of each other or not

class Solution:
    def areRotations(self, s1, s2):
        return s2 in (s1+s1)
