# 20 February 2024
# Word Break

class Solution:
    def wordBreak(self, n, s, dictionary):
        # Complete this function
        dic = {}
        
        for i in dictionary:
            if i in s:
                if i[0] in dic:
                    dic[i[0]].append(i)
                else:
                    dic[i[0]] = [i]
                    
        def solve(st, k, dp):
            if len(st) == k:
                return True
                
            elif dp[k] != None:
                return dp[k]
                
            elif st[k] in dic:
                for i in dic[st[k]]:
                    if len(i) <= len(st[k:]):
                        if st[k:k+len(i)] == i:
                            k += len(i)
                            rt = solve(st, k, dp)
                            
                            if rt:
                                dp[k] = True
                                return True
                            else:
                                k -= len(i)
                
                dp[k] = False
                return False
                
            else:
                dp[k] = False
                return False
                
        dp = [None] * (len(s)+1)
        k = 0
        
        res = solve(s, k, dp)
        return res
