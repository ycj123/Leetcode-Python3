#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #stack
        s1 = []
        s2 = []
        while l1:
            s1.append(l1)
            l1 = l1.next
        while l2:
            s2.append(l2)
            l2 = l2.next
        nxt = None
        carry = 0
        while s1 or s2:
            v1 = s1.pop().val if s1 else 0
            v2 = s2.pop().val if s2 else 0
            carry += v1 + v2
            node = ListNode(carry%10)
            carry//=10
            node.next = nxt
            nxt = node
        if carry:
            tmp = ListNode(1)
            tmp.next = nxt
            nxt = tmp
        return nxt
# @lc code=end

