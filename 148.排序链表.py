#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
# https://leetcode-cn.com/problems/sort-list/description/
#
# algorithms
# Medium (66.87%)
# Likes:    722
# Dislikes: 0
# Total Accepted:    89K
# Total Submissions: 133.1K
# Testcase Example:  '[4,2,1,3]'
#
# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
# 
# 示例 1:
# 
# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 
# 
# 示例 2:
# 
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        slow = fast = dummy
        dummy.next = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow.next = None
        left = head
        leftres = self.sortList(left)
        rightres = self.sortList(right)

        def merge(l, r):
            dummy = ListNode(0)
            p = dummy
            while l and r:
                if l.val > r.val:
                    p.next = r
                    r = r.next
                    p = p.next
                else:
                    p.next = l
                    l = l.next
                    p = p.next
            if l:
                p.next = l
            if r:
                p.next = r
            return dummy.next

        return merge(leftres, rightres)
# @lc code=end
# merge sort
