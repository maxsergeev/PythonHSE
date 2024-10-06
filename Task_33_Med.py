"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
"""

class Solution:
    def search(self, nums, target):
        start, end = 0, len(nums)-1
        while(start<=end):
            mid=int((start + end)/2)
            if nums[mid]==target: return mid
            elif nums[start]<=nums[mid]:
                if target>=nums[start] and target<nums[mid]: end=mid-1
                else: start=mid+1
            else:
                if target<=nums[end] and target>nums[mid]: start=mid+1
                else: end=mid-1
        return -1