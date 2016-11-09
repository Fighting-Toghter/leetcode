# coding: utf-8
"""
@date: 2016/11/9
@author: alric.lin
"""
from unittest import TestCase

from add_two_numbers import Solution, ListNode

class TestSolution(TestCase):

    def setUp(self):
        self.cases = [
            ([2,4,3],[5,6,4],[7,0,8]),
            ([1,8],[0],[1,8]),
                      ]

    def _gen_link_list(self, l):
        if not l:
            return
        head = ListNode(l[0])
        p = head
        for i in l[1:]:
            node = ListNode(i)
            p.next = node
            p = node
        return head

    def _gen_list(self, link_list):
        l = []
        while link_list:
            l.append(link_list.val)
            link_list = link_list.next
        return l

    def test_add_two_numbers(self):
        for case in self.cases:
            l1 = self._gen_link_list(case[0])
            l2 = self._gen_link_list(case[1])
            result = self._gen_list(Solution().addTwoNumbers(l1, l2))
            self.assertEqual(result, case[2])
