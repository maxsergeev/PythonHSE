"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/container-with-most-water/description/
"""

class Solution:
    def maxArea(self, height):
        maxA,L,R = 0,0,len(height)-1
        while R>L:
            lP,rP=height[L],height[R]
            maxA = max(maxA,min(rP,lP)*(R-L))
            if rP>lP : L+=1
            else : R-=1
        return maxA