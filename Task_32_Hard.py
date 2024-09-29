"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-valid-parentheses/description/
"""

class Solution:
    def longestValidParentheses(self, s):
        stack, ans = [-1], 0
        s += "#"   
        for i, c in enumerate(s):  
            if len(stack) > 1 and c == ")" and s[stack[-1]] == "(":
                stack.pop()  
            else:
                ans = max(ans, i - 1 - stack[-1])
                stack.append(i)
        return ans