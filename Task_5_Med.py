"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-palindromic-substring/description/
"""
class Solution:
    def longestPalindrome(self, s):
        ss = ''
        for i in range(len(s)): 
			ss = max(self.checkP(s, i, i), self.checkP(s, i, i + 1), ss, key=len)
        return ss
    def checkP(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]: l -= 1; r += 1
        return s[l+1:r]