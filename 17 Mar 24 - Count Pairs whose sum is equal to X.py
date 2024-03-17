# 17 March 2024
# Count Pairs whose sum is equal to X

class Solution:
    def countPair(self, head1, head2, n1, n2, x):
        '''
        head1:  head of linkedList 1
        head2:  head of linkedList 2
        n1:  len of  linkedList 1
        n2:  len of linkedList 1
        x:   given sum
        '''
        count, new_set = 0, set()
        
        while head2:
            new_set.add(head2.data)
            head2 = head2.next
            
        while head1:
            count += int(x - head1.data in new_set)
            head1 = head1.next
            
        return count
