#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (51.21%)
# Likes:    495
# Dislikes: 0
# Total Accepted:    72.6K
# Total Submissions: 141.4K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
# 
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        def helper(node):#reverse a linkedlist
            pre = None
            while node:
                t = node.next
                node.next = pre
                pre = node
                node = t
            return pre

        dummy = ListNode(0)
        dummy.next = head
        p1 = p2 = dummy
        for _ in range(m-1):
            p1 = p1.next
        for _ in range(n):
            p2 = p2.next
        t1 = p2.next
        p2.next = None
        t2 = p1.next
        p1.next = helper(p1.next)
        t2.next = t1
        return dummy.next
# @lc code=end
# 1 -> 2 -> 3 -> 4 -> 5
# p1  t2         p2   t1

