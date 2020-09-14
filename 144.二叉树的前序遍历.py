#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # res = []
        # def helper(root):
        #     if not root:
        #         return
        #     res.append(root.val)
        #     helper(root.left)
        #     helper(root.right)
        # helper(root)
        # return res

        res = []
        p = root
        stack = []
        while p or stack:
            while p:
                res.append(p.val)
                stack.append(p)
                p = p.left
            p = stack.pop()
            p = p.right
        return res
# @lc code=end
# middle -> left -> right
