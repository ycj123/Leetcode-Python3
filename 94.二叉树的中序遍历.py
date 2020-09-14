#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # res = []
        # def helper(root):
        #     if not root:
        #         return
        #     helper(root.left)
        #     res.append(root.val)
        #     helper(root.right)
        # helper(root)
        # return res

        p = root
        stack = []
        res = []
        while p or stack:
            while p:
                stack.append(p)#all the way to left
                p = p.left
            if stack:
                p = stack.pop()
                res.append(p.val)
                p = p.right
        return res
# @lc code=end
# left -> middle -> right
