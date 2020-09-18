#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
# https://leetcode-cn.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (43.23%)
# Likes:    634
# Dislikes: 0
# Total Accepted:    127.3K
# Total Submissions: 293.6K
# Testcase Example:  '[1,2]'
#
# 请判断一个链表是否为回文链表。
# 
# 示例 1:
# 
# 输入: 1->2
# 输出: false
# 
# 示例 2:
# 
# 输入: 1->2->2->1
# 输出: true
# 
# 
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        pre = None
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            pre, head.next, head = head, pre, head.next
        tail = head.next if fast else head
        while tail:
            if tail.val != pre.val:
                return False
            tail = tail.next
            pre = pre.next
        return True
    def isPalindrome_nicer(self, head):#keep the list unchanged
        rev = None
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, head = head, rev, head.next
        tail = head.next if fast else head
        isPali = True
        while rev:
            isPali = isPali and rev.val == tail.val
            head, head.next, rev = rev, head, rev.next
            tail = tail.next
        return isPali
# @lc code=end
# fast slow pointer:
#  O -> O -> O
# end status : fast is not none slow is at middle 
#  O -> O -> O -> O
# end status : fast is none slow is at right