#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#
# https://leetcode-cn.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (54.55%)
# Likes:    464
# Dislikes: 0
# Total Accepted:    131K
# Total Submissions: 239.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 
# 本题中，一棵高度平衡二叉树定义为：
# 
# 
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
# 
# 
# 示例 1:
# 
# 给定二叉树 [3,9,20,null,null,15,7]
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回 true 。
# 
# 示例 2:
# 
# 给定二叉树 [1,2,2,3,3,null,null,4,4]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
# 
# 
# 返回 false 。
# 
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.res = True
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)+1
            right = helper(node.right) + 1
            if abs(left-right)>1:
                self.res = False
            return max(left, right)
        helper(root)
        return self.res
# @lc code=end

