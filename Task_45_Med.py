"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/jump-game-ii/description/
"""

class Solution:
    def jump(self, nums):
        l,r = 0, 0
        res = 0
        
        while r < len(nums) - 1:
            f = 0
            for i in range(l , r + 1):
                f = max(f, i + nums[i])
            l = r + 1
            r = f
            res += 1
        return res