#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isSym(root.left, root.right)
        
    def isSym(self, l, r):
        if not l and not r: 
            return True
        if l and r and l.val == r.val:
            return self.isSym(l.left, r.right) and self.isSym(l.right, r.left)
        return False
# @lc code=end

root = [1,2,2,3,4,4,3]
method = Solution()
method.isSymmetric(root)