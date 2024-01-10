# 10 January 2024
# Longest subarray with sum divisible by K

class Solution:
    def longSubarrWthSumDivByK (self,arr,  n, k) : 
    #Complete the function
    max_len = 0
    prefix_sum = 0
    remainder_index = {0: -1}
    
    for i in range(n):
        prefix_sum += arr[i]
        remainder = prefix_sum % k
        if remainder in remainder_index:
            # Update max length
            max_len = max(max_len, i - remainder_index[remainder])
        if remainder not in remainder_index:
            remainder_index[remainder] = i
    
    return max_len
