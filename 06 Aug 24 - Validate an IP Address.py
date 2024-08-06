# 06th August 2024
# Validate an IP Address

class Solution:
    def isValid(self, strr):
        #code here
        return all(map(lambda n: 0 <= n <= 255 and len(str(n)) <= 3, map(int, strr.split("."))))
