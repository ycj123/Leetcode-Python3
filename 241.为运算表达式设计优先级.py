#
# @lc app=leetcode.cn id=241 lang=python3
#
# [241] 为运算表达式设计优先级
#
# https://leetcode-cn.com/problems/different-ways-to-add-parentheses/description/
#
# algorithms
# Medium (71.97%)
# Likes:    253
# Dislikes: 0
# Total Accepted:    15.1K
# Total Submissions: 21K
# Testcase Example:  '"2-1-1"'
#
# 给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及
# * 。
# 
# 示例 1:
# 
# 输入: "2-1-1"
# 输出: [0, 2]
# 解释: 
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# 
# 示例 2:
# 
# 输入: "2*3-4*5"
# 输出: [-34, -14, -10, -10, 10]
# 解释: 
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
# 
#

# @lc code=start
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def helper(a, b, op):
            if op=='+':
                return int(a)+int(b)
            elif op=='-':
                return int(a)-int(b)
            else:
                return int(a)*int(b)
        if input.isdigit():
            return [int(input)]
        res = []
        for index,char in enumerate(input):
            if char in {'+','-','*'}:
                left = self.diffWaysToCompute(input[:index])
                right = self.diffWaysToCompute(input[index+1:])
                for i in left:
                    for j in right:
                        res.append(helper(i, j, char))
        return res
# @lc code=end
# for each operator, make it happens last
