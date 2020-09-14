#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#
# https://leetcode-cn.com/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (72.11%)
# Likes:    237
# Dislikes: 0
# Total Accepted:    32.7K
# Total Submissions: 45.3K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# 给出一个完全二叉树，求出该树的节点个数。
# 
# 说明：
# 
# 
# 完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第
# h 层，则该层包含 1~ 2^h 个节点。
# 
# 示例:
# 
# 输入: 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠/ \  /
# 4  5 6
# 
# 输出: 6
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
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftd = self.getDepth(root.left)
        rightd = self.getDepth(root.right)
        if leftd==rightd:
            return pow(2, leftd) + self.countNodes(root.right)
        else:
            return pow(2, rightd) + self.countNodes(root.left)
    
    def getDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.getDepth(root.left)
# @lc code=end
# get depth of left tree and right tree
# compare the depth between left sub tree and right sub tree. 
# 1. If it is equal, it means the left sub tree is a full binary tree
# 2. If it is not , it means the right sub tree is a full binary tree



