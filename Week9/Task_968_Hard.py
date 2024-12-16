"""
leetcode.com/problem-list/binary-tree/
url:https://leetcode.com/problems/binary-tree-cameras/description
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def minCameraCover(self, root):
        self.res = 0
        COVERED = 0
        CAMERA = 1
        NOT_COVERED = 2

        def helper(node):
            if not node:
                return COVERED

            left = helper(node.left)
            right = helper(node.right)

            if left == NOT_COVERED or right == NOT_COVERED:
                self.res += 1
                return CAMERA

            if left == CAMERA or right == CAMERA:
                return COVERED

            return NOT_COVERED

        return (helper(root) == NOT_COVERED) + self.res




