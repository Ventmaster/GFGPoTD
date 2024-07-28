# 28th July 2024
# Remove Duplicates

class Solution:
    def removeDups(self, str):
        # code here
        l = []

        for i in str:
            if i in l:
                continue
            else:
                l.append(i)

        result = "".join(l)

        return result
