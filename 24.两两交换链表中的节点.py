#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        p = head
        pre = dummy
        if not head or not head.next:
            return head
        while p and p.next:
            t = p.next
            pre.next = t
            p.next = t.next
            t.next = p
            pre = p
            p = p.next
        return dummy.next
# @lc code=end

