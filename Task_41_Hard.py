"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/first-missing-positive/description/
"""

class Solution:
    def firstMissingPositive(self, nums):

        nums = set(nums)
        x = 1
        while x in nums:
            x += 1
        return x