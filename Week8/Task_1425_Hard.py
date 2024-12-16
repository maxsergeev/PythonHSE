"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/constrained-subsequence-sum/description
"""

class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        my_deque = deque()
        n=len(nums)
        dp=[0]*n
        print(dp)
        for i, num in enumerate(nums):
            if i > k and my_deque[0] == dp[i-k-1]:
                my_deque.popleft()
            dp[i]=max(my_deque[0] if my_deque else 0,0)+num

            while my_deque and my_deque[-1] <dp[i]:
                my_deque.pop()
            my_deque.append(dp[i])
        return max(dp)      


