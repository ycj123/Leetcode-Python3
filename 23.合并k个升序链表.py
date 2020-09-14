#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (52.66%)
# Likes:    847
# Dislikes: 0
# Total Accepted:    156.1K
# Total Submissions: 296.3K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
# 
# 示例:
# 
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        heap = []
        res = ListNode(0)
        dummy = res
        import heapq
        def __lt__(self,other):#redefine less than func
            return self.val<other.val
        ListNode.__lt__ = __lt__
        for l in lists:
            if l:# do not push None
                heapq.heappush(heap, l)
        while heap:
            curr = heapq.heappop(heap)
            res.next = ListNode(curr.val)
            res = res.next
            if curr.next:
                heapq.heappush(heap, curr.next)
        return dummy.next
# @lc code=end
#heap
