#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#
# https://leetcode-cn.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (53.80%)
# Likes:    380
# Dislikes: 0
# Total Accepted:    35.1K
# Total Submissions: 65K
# Testcase Example:  '10'
#
# 编写一个程序，找出第 n 个丑数。
# 
# 丑数就是质因数只包含 2, 3, 5 的正整数。
# 
# 示例:
# 
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
# 
# 说明:  
# 
# 
# 1 是丑数。
# n 不超过1690。
# 
# 
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0
        while n>1:
            u2, u3, u5 = ugly[i2]*2, ugly[i3]*3, ugly[i5]*5
            umin = min(u2, u3, u5)
            if umin==u2:
                i2 += 1
            if umin==u3:
                i3 += 1
            if umin==u5:
                i5 += 1
            ugly.append(umin)
            n-=1
        return ugly[-1]
# @lc code=end
# can't use elif here : avoid duplicate
