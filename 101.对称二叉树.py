#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def helper(left, right):
            if not left and not right:
                return True
            if not (left and right):
                return False  
            if left.val != right.val:
                return False
            return helper(left.left, right.right)\
                 and helper(left.right, right.left)
        return helper(root.left,root.right)
# @lc code=end

