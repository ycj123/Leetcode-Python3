#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#
# https://leetcode-cn.com/problems/single-number-iii/description/
#
# algorithms
# Medium (73.57%)
# Likes:    286
# Dislikes: 0
# Total Accepted:    29.9K
# Total Submissions: 40.6K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。
# 
# 示例 :
# 
# 输入: [1,2,1,3,2,5]
# 输出: [3,5]
# 
# 注意：
# 
# 
# 结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
# 你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
# 
# 
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        mask = xor&(-xor)
        res1 = res2 = 0
        for num in nums:
            if num&mask==0:
                res1 ^= num
            else:
                res2 ^= num
        return [res1, res2]
# @lc code=end
# 1.把所有的元素进行异或操作，最终得到一个异或值。因为是不同的两个数字，所以这个值必定不为0；
# 2.取异或值最后一个二进制位为1的数字作为mask，如果是1则表示两个数字在这一位上不同。
# 3.通过与这个mask进行与操作，如果为0的分为一个数组，为1的分为另一个数组。
# 这样就把问题降低成了：“有一个数组每个数字都出现两次，有一个数字只出现了一次，求出该数字”。
# 对这两个子问题分别进行全异或就可以得到两个解。也就是最终的数组了。

# 最后一个二进制位为1的数 ： num & (-num)