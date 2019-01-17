#https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current = dummy
        k = 0

        while l1 or l2:
            sum = k
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            if sum > 9:
                k = 1
                sum -= 10
            else:
                k = 0

            current.next = ListNode(sum)
            current = current.next

        if k != 0:
            current.next = ListNode(k)

        return dummy.next