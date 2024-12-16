"""
leetcode.com/problem-list/binary-tree/
url:https://leetcode.com/problems/recover-binary-search-tree/description
"""

class Solution(object):
    def inorder(self, root, nodes, vals):
        if not root:
            return
        self.inorder(root.left, nodes, vals)
        nodes.append(root)
        vals.append(root.val)
        self.inorder(root.right, nodes, vals)

    def recoverTree(self, root):
        nodes = []
        vals = []
        self.inorder(root, nodes, vals)
        new_vals = sorted(vals)
        idxes = []
        for idx in range(len(vals)):
            if vals[idx] != new_vals[idx]:
                idxes.append(idx)
        nodes[idxes[0]].val, nodes[idxes[1]].val = \
            nodes[idxes[1]].val, nodes[idxes[0]].val



