#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#
# https://leetcode-cn.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (49.41%)
# Likes:    403
# Dislikes: 0
# Total Accepted:    78.3K
# Total Submissions: 158.1K
# Testcase Example:  '"25525511135"'
#
# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
# 
# 有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
# 
# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312"
# 和 "192.168@1.1" 是 无效的 IP 地址。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]
# 
# 
# 示例 2：
# 
# 输入：s = "0000"
# 输出：["0.0.0.0"]
# 
# 
# 示例 3：
# 
# 输入：s = "1111"
# 输出：["1.1.1.1"]
# 
# 
# 示例 4：
# 
# 输入：s = "010010"
# 输出：["0.10.0.10","0.100.1.0"]
# 
# 
# 示例 5：
# 
# 输入：s = "101023"
# 输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= s.length <= 3000
# s 仅由数字组成
# 
# 
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []

        def helper(index, path, flag):
            if index == n and flag==0:
                res.append(path[:-1])
            if flag==0:
                return
            for j in range(index, index+3):# a. ab. abc.
                if j >= n:
                    break
                if index==j and s[index] == '0':
                    helper(j+1, path+'0.', flag-1)
                    break
                if 0 < int(s[index:j+1]) <= 255:
                    helper(j+1, path+s[index:j+1]+'.', flag-1)

        helper(0, '', 4)
        return res
# @lc code=end
# backtrack
# special case: 01 is wrong
