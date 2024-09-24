# 24th September 2024
# Smallest window in a string containing all the characters of another string

class Solution:
    def smallestWindow(self, s, p):
       
        sAlpha,pAlpha = [0]*26,[0]*26
        ct1 = ct2 = ind = 0
        
        mn = float('inf')
        res = ''
        
        for idx in p: 
            pAlpha[ord(idx)-97]+=1
            if pAlpha[ord(idx)-97] == 1: ct1+=1
            
        for l,(idx) in enumerate(s): 
            sAlpha[ord(idx)-97]+=1
            
            if sAlpha[ord(idx)-97] == pAlpha[ord(idx)-97]: ct2+=1
            
            if ct1 == ct2:
                
                while sAlpha[ord(s[ind])-97] > pAlpha[ord(s[ind])-97]: 
                    sAlpha[ord(s[ind])-97]-=1
                    ind += 1
                    
                if mn > (l - ind + 1):
                    mn = (l - ind + 1)
                    res = s[ind:l+1]
                
        return res if mn != float('inf') else '-1'

