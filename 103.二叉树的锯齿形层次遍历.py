#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        from collections import deque
        queue = deque()
        queue.append(root)
        index = 1
        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if not index & 0x1 :
                level[:] = level[::-1]
            res.append(level)
            index += 1
        return res
# @lc code=end

