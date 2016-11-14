# coding: utf-8
"""
@date: 2016/11/14
@author: alric.lin
"""
class Solution(object):
    def badLengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        效率很低.遍历所有可能情况.
        """
        length = len(s)
        if length == 0:
            return 0
        if length == 1:
            return 1
        records = []
        for i in range(length-1):
            for j, v in enumerate(s[i+1:]):
                substring = s[i:i+1+j]
                if v in substring:
                    records.append(len(substring))
                    break
                elif i+j+1 == length-1:
                    records.append(len(substring)+1)
        return max(records)

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        每次搜索delta长度的字符串.保证下次delta迭代大于等于上次
        """
        length = len(s)
        if length == 0:
            return 0
        if length == 1:
            return 1

        delta = 1
        i = 0
        j = 1
        while True:
            j = i+1+delta
            if j > length:
                break
            if len(s[i: j]) == len(set(s[i: j])):
                delta +=1
            else:
                i += 1

        return delta

