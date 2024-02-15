# 15 February 2024
# Count all Possible Path

class Solution:
    def isPossible(self, paths):
        # Code here
        for i in paths:
            if i.count(1) % 2:
                return 0

        return 1
