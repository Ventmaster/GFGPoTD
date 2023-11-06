# 05 Nov 2023
# Top K Frequent Elements in Array - |

class Solution:
    def topK(self, nums, k):
        #Code here

        d = {}
        answer = []

        for i in nums:
            d[i] = d.get(i,0) + 1

        d = sorted(d.items(), key = lambda x: [x[1],x[0]], reverse = True)

        for i in range(k):
            answer.append(d[i][0])

        return answer
