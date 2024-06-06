# 06th June 2024
# Max sum in the configuration

def max_sum(a,n):
    #code here
    s0 = sum(i * a[i] for i in range(n))
    sum_a = sum(a)
    result = s0
    current_sum = s0
    
    for k in range(1, n):
        current_sum += sum_a - n * a[n - k]
        
        if current_sum > result:
            result = current_sum
            
    return result
