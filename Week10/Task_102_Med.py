"""
leetcode.com/problem-list/binary-tree/
url:https://leetcode.com/problems/binary-tree-level-order-traversal/description
"""

class Solution(object):
    def levelOrder(self, root):
        
        def _level(root, level, dict_levels):
            if root is None:
                return
            dict_levels[level] = dict_levels.get(level, []) + [root.val]
            _level(root.left, level + 1, dict_levels)
            _level(root.right, level + 1, dict_levels)
            
        d = {}
        _level(root, 0, d)
        return d.values()




