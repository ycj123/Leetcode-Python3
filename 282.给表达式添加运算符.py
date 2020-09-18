#
# @lc app=leetcode.cn id=282 lang=python3
#
# [282] 给表达式添加运算符
#
# https://leetcode-cn.com/problems/expression-add-operators/description/
#
# algorithms
# Hard (34.57%)
# Likes:    141
# Dislikes: 0
# Total Accepted:    4K
# Total Submissions: 11.4K
# Testcase Example:  '"123"\n6'
#
# 给定一个仅包含数字 0-9 的字符串和一个目标值，在数字之间添加二元运算符（不是一元）+、- 或 * ，返回所有能够得到目标值的表达式。
# 
# 示例 1:
# 
# 输入: num = "123", target = 6
# 输出: ["1+2+3", "1*2*3"] 
# 
# 
# 示例 2:
# 
# 输入: num = "232", target = 8
# 输出: ["2*3+2", "2+3*2"]
# 
# 示例 3:
# 
# 输入: num = "105", target = 5
# 输出: ["1*0+5","10-5"]
# 
# 示例 4:
# 
# 输入: num = "00", target = 0
# 输出: ["0+0", "0-0", "0*0"]
# 
# 
# 示例 5:
# 
# 输入: num = "3456237490", target = 9191
# 输出: []
# 
# 
#

# @lc code=start
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        def helper(num:str, path:str, pre:int, sum_:int):
            if not num:#no more candidates
                if sum_==target:#match target
                    res.append(path)

            for i in range(1, len(num)+1):#divide current num
                if i>1 and num[0]=='0':# 05 is not right
                    break
                curr = num[:i]#left half 
                curr_num = int(curr)
                if not path:#begining of expression
                    helper(num[i:], curr, curr_num, int(curr))
                    continue
                helper(num[i:], path+'+'+curr, curr_num, sum_+curr_num)
                helper(num[i:], path+'-'+curr, -curr_num, sum_-curr_num)
                helper(num[i:], path+'*'+curr, pre*curr_num, sum_-pre+pre*curr_num)#*
        helper(num, '', 0, 0)
        return res
# @lc code=end
# backtrack
# place op in each gap
# multiple : higher priority -> memory pre result