#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def __lt__(self, other):
            return self.val < other.val
        ListNode.__lt__ = __lt__
        heap = []
        import heapq
        res = head = ListNode(0)
        for i in lists:
            if i:
                heapq.heappush(heap,i)
        while heap:
            node = heapq.heappop(heap)
            res.next = ListNode(node.val)
            res = res.next
            if node.next:
                heapq.heappush(heap,node.next)
        return head.next
# @lc code=end

