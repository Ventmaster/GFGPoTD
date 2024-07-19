# 19 July 2024
# Count Smaller elements

class Solution:
    def mergesort(self, num):
        half = len(num) // 2
        
        if half:
            left, right = self.mergesort(num[:half]), self.mergesort(num[half:])
            
            for i in range(len(num)-1, -1, -1):
                if not right or left and left[-1][1] > right[-1][1]:
                    self.smaller[left[-1][0]] += len(right)
                    num[i] = left.pop()
                else:
                    num[i] = right.pop()
                    
        return num

	def constructLowerArray(self,arr):
		# code here
        self.smaller = [0] * len(arr)
        self.mergesort(list(enumerate(arr)))
        
        return self.smaller
