# 29th October 2024
# Quick Sort on Linked List

class Solution:
    def quickSort(self, head):
        return self.quickSortRecur(head, self.getTail(head))

    def getTail(self, node):
        # Find the tail node of the list
        while node is not None and node.next is not None:
            node = node.next
        return node

    def quickSortRecur(self, head, end):
        # Base case: if head is empty or is the same as end
        if head is None or head == end:
            return head

        # Partition the list, newHead and newEnd will hold the new head and tail of the list
        newHead, newEnd, pivot = self.partition(head, end)

        # If the pivot is not the smallest element, recursively sort the left side
        if newHead != pivot:
            temp = newHead
            while temp.next != pivot:
                temp = temp.next
            temp.next = None  # Break the list

            # Recur for the list before pivot
            newHead = self.quickSortRecur(newHead, temp)

            # Reconnect pivot to the end of the left sorted list
            temp = self.getTail(newHead)
            temp.next = pivot

        # Recur for the list after the pivot element
        pivot.next = self.quickSortRecur(pivot.next, newEnd)

        return newHead

    def partition(self, head, end):
        # Partition using end as pivot, return the pivot's position
        pivot = end
        prev, curr = None, head
        tail = pivot

        # Track the new head and new end
        newHead, newEnd = None, tail

        while curr != pivot:
            if curr.data < pivot.data:
                if newHead is None:
                    newHead = curr
                prev = curr
                curr = curr.next
            else:
                # Move curr to the end of the list
                if prev:
                    prev.next = curr.next
                temp = curr.next
                curr.next = None
                tail.next = curr
                tail = curr
                curr = temp

        if newHead is None:
            newHead = pivot

        newEnd = tail

        return newHead, newEnd, pivot

# Add this function to the Solution class
def quickSort(head):
    solution = Solution()
    return solution.quickSort(head)
