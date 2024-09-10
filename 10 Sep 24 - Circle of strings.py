# 10th September 2024
# Circle of strings

from collections import defaultdict

class Solution:
    def isCircle(self, arr):
        # code here
        d = defaultdict(list)
        visited = set()
        
        def char_to_index(c):
            return ord(c) - ord('a')
        
        in_ = [0] * 26
        out = [0] * 26
        
        for s in arr:
            first = char_to_index(s[0])
            last = char_to_index(s[-1])
            in_[first] += 1
            out[last] += 1
            d[first].append(last)
            
        if in_ != out:
            return 0
            
        st = [char_to_index(arr[0][0])]
        
        while st:
            c = st.pop()
            
            if c not in visited:
                visited.add(c)
                
                for i in d[c]:
                    st.append(i)
                    
        if len(visited) != len(d):
            return 0
            
        return 1
