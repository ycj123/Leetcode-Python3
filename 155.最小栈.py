#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#
# https://leetcode-cn.com/problems/min-stack/description/
#
# algorithms
# Easy (55.22%)
# Likes:    656
# Dislikes: 0
# Total Accepted:    159.1K
# Total Submissions: 288K
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n' +
  '[[],[-2],[0],[-3],[],[],[],[]]'
#
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
# 
# 
# push(x) —— 将元素 x 推入栈中。
# pop() —— 删除栈顶的元素。
# top() —— 获取栈顶元素。
# getMin() —— 检索栈中的最小元素。
# 
# 
# 
# 
# 示例:
# 
# 输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 
# 输出：
# [null,null,null,null,-3,null,0,-2]
# 
# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
# 
# 
# 
# 
# 提示：
# 
# 
# pop、top 和 getMin 操作总是在 非空栈 上调用。
# 
# 
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.cur_min = float("inf")
        

    def push(self, x: int) -> None:
        if x <= self.cur_min:
            self.stack.append(self.cur_min)
            self.cur_min = x
        self.stack.append(x)
        

    def pop(self) -> None:
        if self.stack.pop() == self.cur_min:
            self.cur_min = self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.cur_min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
# memory pre min under current min
