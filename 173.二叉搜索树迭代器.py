#
# @lc app=leetcode.cn id=173 lang=python3
#
# [173] 二叉搜索树迭代器
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.push_back(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        curr = self.stack.pop()
        if curr.right:
            self.push_back(curr.right)
        return curr.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.stack: 
            return True
        else:
            return False
    def push_back(self, root: TreeNode):
        while root:
            self.stack.append(root)
            root = root.left



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end
# inorder left -> middle -> right
