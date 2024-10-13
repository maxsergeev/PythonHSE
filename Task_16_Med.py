"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/3sum-closest/description/
"""

class Solution:
    def threeSumClosest(self, nums, target):
        res=sum(nums[:3])
        for i in range(0,len(nums)):
            j=i+1
            g=len(nums)-1
            while(j<g):
                s = sum((nums[i], nums[j], nums[g]))
                if(abs(s-target) <abs(res-target)):
                    res=s
                if(s<target):
                    j+=1
                elif(s>target):
                    g-=1
                else:
                    return res
        return res