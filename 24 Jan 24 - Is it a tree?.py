class Solution:
    def isTree(self, n, m, edges):
        # Code here
        parent = list(range(n))
        rank = [0] * n
        
        def finding(k):
            if parent[k] != k:
                parent[k] = finding(parent[k])
            return parent[k]
            
        def if_union_is_different(k, l):
            parent_k, parent_l = finding(k), finding(l)
            
            if parent_k == parent_l:
                return False
                
            rank_k, rank_l = rank[parent_k], rank[parent_l]
            
            if rank_k > rank_l:
                parent[parent_l] = parent_k
            elif rank_l > rank_k:
                parent[parent_k] = parent_l
            else:
                parent[parent_l] = parent_k
                rank[parent_k] += 1
            
            return True
            
        for u, v in edges:
            if not if_union_is_different(u, v):
                return 0
                
        root = finding(parent[0])
        
        return 1 if all(finding(p) == root for p in parent) else 0
