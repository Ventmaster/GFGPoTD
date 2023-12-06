class Solution:
    def countX(self, L, R, X):
        X = str(X)
        result = 0

        for i in range(L+1, R):
            i = str(i)
            result += i.count(X)

        return result 
