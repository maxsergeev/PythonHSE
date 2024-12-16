"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/max-value-of-equation/description
"""


class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        elements = deque()
        res = -float("inf")
        for x,y in points:
            while elements and elements[0][1] < x-k:
                elements.popleft()
            if elements:
                res = max(res,elements[0][0]+y+x)
            while elements and elements[-1][0] <= y-x:
                elements.pop()
            elements.append([y-x,x])
        
        return res



