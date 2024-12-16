"""
leetcode.com/problem-list/binary-tree/
url:https://leetcode.com/problems/balance-a-binary-search-tree/description
"""

class Solution(object):
    def balanceBST(self, root):
        self.arr = []
        def inOrder(root):
            if root is None: return 
            
            inOrder(root.left)
            self.arr.append(root.val)
            inOrder(root.right)
        def buildTree(inorder):
            if not inorder: return
            idx = len(inorder) // 2
            root = TreeNode(val=inorder[idx])
            root.left = buildTree(inorder[:idx])
            root.right = buildTree(inorder[idx + 1:])
            return root
        inOrder(root)
        return buildTree(self.arr)



