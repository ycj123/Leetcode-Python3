#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#
# https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (76.05%)
# Likes:    356
# Dislikes: 0
# Total Accepted:    59.6K
# Total Submissions: 78.4K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
# 
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
# 
# 示例:
# 
# 给定的有序链表： [-10, -3, 0, 5, 9],
# 
# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def findmid(head, tail):
            slow = head
            fast = head
            while fast!=tail and fast.next!=tail:
                slow = slow.next
                fast = fast.next.next
            return slow
        def helper(head, tail):
            if head==tail:
                return None
            mid = findmid(head, tail)
            root = TreeNode(mid.val)
            root.left = helper(head, mid)
            root.right = helper(mid.next, tail)
            return root
        return helper(head, None)
            
# @lc code=end
# find middle node
# left tree base on the node before middle node
# right tree base on the node after middle node
