# 16 April 2024
# Minimize the Difference

from typing import List


class Solution:
    def minimizeDifference(self, n : int, k : int, arr : List[int]) -> int:
        max_from_right = [0 for _ in range(n)]
        min_from_right = [0 for _ in range(n)]
        max_from_left = [0 for _ in range(n)]
        min_from_left = [0 for _ in range(n)]
        min_from_left[0] = arr[0]
        max_from_left[0] = arr[0]
        answer = float("inf")
        for i in range(1 , n):
            max_from_left[i] = max(arr[i] , max_from_left[i-1])
            min_from_left[i] = min(arr[i] , min_from_left[i-1])
        max_from_right[n-1] = arr[-1]
        min_from_right[n-1] = arr[-1]
        for i in range(n-2 , -1 , -1):
            max_from_right[i] = max(max_from_right[i+1] , arr[i])
            min_from_right[i] = min(min_from_right[i+1] , arr[i])
        for i in range(n) :
            a , b = [min_from_left[i-1] , max_from_left[i-1]] if i-1>=0 else [float("inf") , float("-inf")]
            c , d = [min_from_right[i+k] , max_from_right[i+k]] if i+k < n else [float("inf") , float("-inf")]
            answer = min( max(b,d) - min(a,c)  , answer  )
        return answer
