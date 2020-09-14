#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_s = float('-inf')
        
        def helper(node):
            if not node:
                return 0
            leftmax = max(0, helper(node.left))
            rightmax = max(0, helper(node.right))
            self.max_s = max(self.max_s, leftmax+rightmax+node.val)
            return node.val + max(leftmax,rightmax)
        
        helper(root)
        return self.max_s
# @lc code=end
# current node -> root
# in left tree
# in right tree
