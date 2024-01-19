# 19 January 2024
# Top k numbers in a stream

class Solution:
    def kTop(self,a, N, K):
        #code here.
        result = []
        top = [0 for i in range(K+1)]
        frequency = {i:0 for i in range(K+1)}
        
        for m in range(N):
            if a[m] in frequency.keys():
                frequency[a[m]] += 1
            else:
                frequency[a[m]] = 1
                
            top[k] = a[m]
            i = top.index(a[m])
            i -= 1
            
            while i >= 0:
                if (frequency[top[i]] < frequency[top[i+1]]):
                    t = top[i]
                    top[i] = top[i+1]
                    top[i+1] = t
                    
                elif ((frequency[top[i]] == frequency[top[i+1]]) and (top[i] > top[i+1])):
                    t = top[i]
                    top[i] = top[i+1]
                    top[i+1] = t
                
                else:
                    break
                i -= 1
                
            i = 0
            ans = []
            
            while i < K and top[i] != 0:
                ans.append(top[i])
                i = i + 1
                
            result += [ans]
            
        return result 
