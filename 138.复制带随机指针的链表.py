#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        dummy = head
        helper = {} # map old -> new
        while head:
            if head not in helper:
                helper[head] = Node(head.val)
            if head.next:
                if head.next not in helper:
                    helper[head.next] = Node(head.next.val)
                helper[head].next = helper[head.next]
            if head.random:
                if head.random not in helper:
                    helper[head.random] = Node(head.random.val)
                helper[head].random = helper[head.random]
            head = head.next
        return helper[dummy]
# @lc code=end
# map
