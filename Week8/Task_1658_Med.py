"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description
"""


class Solution(object):
    def minOperations(self, nums, x):
        target = sum(nums) - x
        if target == 0:
            return len(nums)
    
        left = 0
        current_sum = 0
        max_length = float('-inf')

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1

            if current_sum == target:
                max_length = max(max_length, right - left + 1)

        if max_length == float('-inf'):
            return -1
        else:
            return len(nums) - max_length



