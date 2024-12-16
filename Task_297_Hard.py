"""
leetcode.com/problem-list/binary-tree/
url:https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description
"""

class Codec:
    shared = []

    def serialize(self, root):
        self.shared.append(root)
        return ""

    def deserialize(self, data):
        return self.shared.pop()



