#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        from collections import deque
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            pre = queue.popleft()
            if pre.left:
                queue.append(pre.left)
            if pre.right:
                queue.append(pre.right)
            for _ in range(size-1):
                curr = queue.popleft()
                pre.next = curr
                pre = curr
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return root
# @lc code=end

