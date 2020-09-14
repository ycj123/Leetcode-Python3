#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 两数相加 个位在前
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        remaining = 0# carry number of add
        res = head = ListNode(0)
        while l1 or l2:
            t1 = l1.val if l1 else 0
            t2 = l2.val if l2 else 0
            remaining += t1 + t2
            res.next = ListNode(remaining%10)
            remaining //= 10
            res = res.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if remaining:# carry 1
            res.next = ListNode(remaining)
        return head.next
# @lc code=end

