#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#
# https://leetcode-cn.com/problems/single-number-ii/description/
#
# algorithms
# Medium (67.84%)
# Likes:    412
# Dislikes: 0
# Total Accepted:    40.5K
# Total Submissions: 59.8K
# Testcase Example:  '[2,2,3,2]'
#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
# 
# 说明：
# 
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
# 
# 示例 1:
# 
# 输入: [2,2,3,2]
# 输出: 3
# 
# 
# 示例 2:
# 
# 输入: [0,1,0,1,0,1,99]
# 输出: 99
# 
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = [0]*32
        for num in nums:
            for j in range(32):
                count[j] += num&0x1
                num >>= 1
        res = 0
        for i in range(32):
            res <<= 1
            res |= count[31-i] % 3
        return res if count[31]%3==0 else ~(res ^ 0xffffffff)
# @lc code=end
# 由于 Python 的存储负数的特殊性，需要先将 0 - 32 位取反
# （即 res ^ 0xffffffff ），再将所有位取反（即 ~ ）。
# 两个组合操作实质上是将数字 32 以上位取反， 0 - 32 位不变。

