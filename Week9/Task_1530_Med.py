"""
leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/description
"""

class Solution(object):
    def countPairs(self, root, distance):
        ans = [0]
        def dfs(node):
            if not node:
                return []
            if not (node.left or node.right):
                return [1]
                
            l = dfs(node.left)
            r = dfs(node.right)

            for i in l:
                for j in r:
                    if i + j <= distance:
                        ans[0] += 1
            return [i + 1 for i in l + r]

        dfs(root)
        return ans[0]



