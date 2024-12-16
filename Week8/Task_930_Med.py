"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/binary-subarrays-with-sum/description
"""


class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        if goal<0 or len(nums)<goal:
            return 0
        curr_sum =   0
        prefix_zero = 0
        l = 0
        total = 0
        for r in range(len(nums)):
            curr_sum+=nums[r]
            while l<r and (nums[l]==0 or curr_sum>goal):
                if nums[l]==1:
                    prefix_zero = 0
                    curr_sum-=nums[l]
                else:
                    prefix_zero+=1
                l+=1
            if curr_sum == goal:
                total+= (1+prefix_zero)
        return total

