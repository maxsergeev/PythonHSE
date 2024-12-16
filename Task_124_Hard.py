"""
leetcode.com/problem-list/binary-tree/
url:https://leetcode.com/problems/binary-tree-maximum-path-sum/description
"""

class Solution:
    def maxPathSum(self, root):
        self.ans = float('-inf')
        def PathSum(node):
            if not node: return 0
            left,right = PathSum(node.left),PathSum(node.right)
            self.ans = max(self.ans, node.val+left+right)
            return max(0, node.val+left, node.val+right)
        PathSum(root)
        return self.ans



