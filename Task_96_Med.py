"""
leetcode.com/problem-list/binary-tree/
url:https://leetcode.com/problems/unique-binary-search-trees/description
"""

class Solution(object):
    def numTrees(self, n):

        a = [0] * (n + 1)
        a[0], a[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(i):
                a[i] += a[j] * a[i - j - 1]
        return a[-1]