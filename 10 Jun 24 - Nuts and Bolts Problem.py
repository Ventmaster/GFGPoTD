# 10th June 2024
# Nuts and Bolts Problem

class Solution:
    def matchPairs(self, n, nuts, bolts):
        # code here
	order = ['!','#','$','%','&','*','?','@','^']
	order_d = {v:i for i,v in enumerate(order)}
	nuts_set = set(nuts)
	bolts_set = set(bolts)
	common = nuts_set.intersection(bolts_set)
	result_d = {}
        
        for k, v in order_d.items():
            if k in common:
                result_d[k] = v
            else:
                continue
            
        sorted_d = sorted(result_d.items(), key = lambda x: x[1])
        
        for i, (key, _) in enumerate(sorted_d):
            nuts[i] = key
            bolts[i] = key
            
        return nuts, bolts
