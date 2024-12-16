"""
leetcode.com/problem-list/binary-tree/
url:https://leetcode.com/problems/validate-binary-search-tree/description
"""

class Solution(object):
    def isValidBST(self, root):
        stack = [None]
        prev = -float("inf")
        while stack:
            while root:
                stack.append(root)
                root = root.left
            x = stack.pop()
            if x:
                if x.val <= prev:
                    return False
                prev = x.val
                root = x.right
                
        return True
