#
# @lc app=leetcode.cn id=233 lang=python3
#
# [233] 数字 1 的个数
#
# https://leetcode-cn.com/problems/number-of-digit-one/description/
#
# algorithms
# Hard (37.35%)
# Likes:    161
# Dislikes: 0
# Total Accepted:    10.7K
# Total Submissions: 28.5K
# Testcase Example:  '13'
#
# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
# 
# 示例:
# 
# 输入: 13
# 输出: 6 
# 解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。
# 
#

# @lc code=start
class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        i = 1
        while i<=n:
            xyzd = n//i
            abc = n % i
            xyz = xyzd // 10
            d = xyzd % 10
            count += xyz*i
            if d==1:
                count += abc + 1
            elif d>1:
                count += i
            i *= 10
        return count
# @lc code=end
# 假设 n = xyzdabc，此时我们求千位是 1 的个数，也就是 d 所在的位置。

# 那么此时有三种情况，

# d == 0，那么千位上 1 的个数就是 xyz * 1000
# d == 1，那么千位上 1 的个数就是 xyz * 1000 + abc + 1
# d > 1，那么千位上 1 的个数就是 xyz * 1000 + 1000

