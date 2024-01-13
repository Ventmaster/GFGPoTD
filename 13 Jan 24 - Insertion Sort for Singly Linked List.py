# 13 January 2024
# Insertion Sort for Singly Linked List

class Solution:
    def insertionSort(self, head):
        sorted_list = None

        while head is not None:
            current = head
            head = head.next

            if sorted_list is None or current.data < sorted_list.data:
                current.next = sorted_list
                sorted_list = current
            else:
                temp = sorted_list
                while temp.next is not None and temp.next.data < current.data:
                    temp = temp.next
                current.next = temp.next
                temp.next = current

        return sorted_list
