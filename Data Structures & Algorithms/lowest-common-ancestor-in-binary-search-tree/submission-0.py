# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root
        while node:
            v = node.val
            if p.val < v and q.val < v:
                node = node.left
            elif p.val > v and q.val > v:
                node = node.right
            else:
                return node