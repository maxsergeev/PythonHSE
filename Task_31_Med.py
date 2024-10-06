"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/next-permutation/description/
"""

class Solution:
    def find_min(self,matrix,i):
        for j in range(len(matrix)-1,i,-1):
            if matrix[j] > matrix[i]:
                matrix[i],matrix[j] = matrix[j],matrix[i]
                break

        matrix[i+1:] = reversed(matrix[i+1:])

    def nextPermutation(self, nums):
        index = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                index = i
                break
        
        if index == -1: return nums.reverse()
        
        self.find_min(nums,index)

        return nums