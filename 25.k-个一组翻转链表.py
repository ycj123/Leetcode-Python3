#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def helper(p):#reverse a linked list
            pre = None
            curr = p
            while curr:
                t = curr.next
                curr.next = pre
                pre = curr
                curr = t
            return pre

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        end = dummy
        while end.next:
            start = pre.next#first node
            for i in range(k):
                end = end.next#kth node
                if not end:#shorter than k do not reverse
                    break
            if not end:
                break
            t = end.next#store the begin of next k
            end.next = None#split current k
            pre.next = helper(start)#reverse current k and link the head
            start.next = t#link the tail
            end = start
            pre = start
        return dummy.next
# @lc code=end

