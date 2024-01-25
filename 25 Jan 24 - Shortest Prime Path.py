# 25 January 2024
# Shortest Prime Path

from collections import deque
import math

class Solution:
    def solve (self,num1,num2):
        #code here
        num1=str(num1)
        num2=str(num2)
        
        def isprime(num):
            for i in range(2,int(math.sqrt(num))+1):
                if num%i==0:
                    return False
            return True
        
        ans=0
        q=deque()
        q.append([num1,0])
        vis={num1}
        while q:
            p,cnt=q.pop()
            if p==num2:
                return cnt
            for i in range(4):
                if i!=0:
                    s1=p[:i]
                    s2=p[i+1:]
                    s=s1+str(0)+s2
                    if s not in vis and isprime(int(s)):
                        q.appendleft([s,cnt+1])
                        vis.add(s)
                for j in range(1,10):
                    s1=p[:i]
                    s2=p[i+1:]
                    s=s1+str(j)+s2
                    if s not in vis and isprime(int(s)):
                        q.appendleft([s,cnt+1])
                        vis.add(s)
        return 0
