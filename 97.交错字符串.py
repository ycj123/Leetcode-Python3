#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#
# https://leetcode-cn.com/problems/interleaving-string/description/
#
# algorithms
# Hard (45.25%)
# Likes:    334
# Dislikes: 0
# Total Accepted:    35.3K
# Total Submissions: 78K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# 给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。
# 
# 
# 
# 示例 1：
# 
# 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 输出：true
# 
# 
# 示例 2：
# 
# 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 输出：false
# 
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        import functools
        @functools.lru_cache(None)
        def helper(i, j, k):# top down
            if i==n1 and j==n2 and k==n3:
                return True
            if k<n3:
                if i<n1 and s1[i]==s3[k]:
                    if helper(i+1, j, k+1):
                        return True
                if j<n2 and s2[j]==s3[k]:
                    if helper(i, j+1, k+1):
                        return True
            return False
        return helper(0,0,0)
# @lc code=end
#dynamic planning
