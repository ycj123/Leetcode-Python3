#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (51.33%)
# Likes:    388
# Dislikes: 0
# Total Accepted:    136.7K
# Total Submissions: 266.1K
# Testcase Example:  '[1,1,2]'
#
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
# 
# 示例 1:
# 
# 输入: 1->1->2
# 输出: 1->2
# 
# 
# 示例 2:
# 
# 输入: 1->1->2->3->3
# 输出: 1->2->3
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre = dummy = ListNode(0)
        dummy.next = head
        while head:
            if head.next and head.val==head.next.val:
                value = head.val
                while head.next and head.next.val==value:
                    head = head.next
            else:
                pre.next = head
                pre = pre.next
                head = head.next
        return dummy.next
# @lc code=end

