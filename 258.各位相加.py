#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        return 0 if num==0 else (num-1)%9 + 1
# @lc code=end
# digital root 数根
# （1）  9加上任何正整数所得的和的数字根，等于原来数字的数字根   
# （2）  9乘以任何正整数所得的积的数字根为9 
# （3）两个正整数相加，原来两个数的数字根之和等于和的数字根  
# （4） 两个正整数相乘，原来两个数的数字根之积等于积的数字根

