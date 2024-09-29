"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-common-subsequence/description/
"""

class Solution:
    def longestCommonSubsequence(self, text1, text2):
        dp = [[0 for i in range(len(text1)+1)] for i in range(len(text2)+1)]
        for r in range(1, len(text2)+1):
            for c in range(1, len(text1)+1):
                if text1[c-1] == text2[r-1]:
                    dp[r][c] = dp[r-1][c-1] + 1
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])
        return dp[-1][-1]