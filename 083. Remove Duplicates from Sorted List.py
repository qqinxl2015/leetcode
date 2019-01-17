#https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None:
            return None
        
        answer = head
        while head is not None:
            if head.next is not None:
                while head.next is not None and head.val == head.next.val:
                    head.next = head.next.next
            head = head.next
        return answer