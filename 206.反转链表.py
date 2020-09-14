#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def helper(head):
            if not head:
                return head
            pre = None
            dummy = head
            while head:
                t = head.next
                head.next = pre
                pre = head
                head = t
            return pre
        return helper(head)
# @lc code=end

