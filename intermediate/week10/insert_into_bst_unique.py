# Author: Melissa Marie Perez
# Date: 7/30/2022
# Description:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertIntoBST(root, val: int):
    if not root:
        root = TreeNode(val)
        return root
    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)
    return root
