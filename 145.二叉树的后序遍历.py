#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # res = []
        # def helper(root):
        #     if not root:
        #         return
        #     helper(root.left)
        #     helper(root.right)
        #     res.append(root.val)
        # helper(root)
        # return res

        res = []
        stack = []
        p = root
        while p or stack:
            while p:#all the way down
                stack.append(p)
                if p.left:
                    p = p.left
                else:
                    p = p.right
            p = stack.pop()
            res.append(p.val)
            if stack and stack[-1].left==p:#is left tree
                p = stack[-1].right
            else:#is not left tree
                p = None
        return res
# @lc code=end
# left -> right -> middle
