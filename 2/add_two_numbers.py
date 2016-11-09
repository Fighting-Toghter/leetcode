# coding: utf-8
"""
@date: 2016/11/9
@author: alric.lin
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = 0
        b = 0

        i = 0
        while l1:
            a += l1.val * 10**i
            l1 = l1.next
            i += 1

        i = 0
        while l2:
            b += l2.val * 10**i
            l2 = l2.next
            i +=1

        c = str(a + b)
        head = ListNode(c[-1])
        node = head
        for i in c[-2::-1]:
            next_node = ListNode(i)
            node.next = next_node
            node = next_node

        return head