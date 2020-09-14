#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#
# https://leetcode-cn.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (45.26%)
# Likes:    116
# Dislikes: 0
# Total Accepted:    22.5K
# Total Submissions: 49.7K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# 所有 DNA 都由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA
# 中的重复序列有时会对研究非常有帮助。
# 
# 编写一个函数来查找目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。
# 
# 
# 
# 示例：
# 
# 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出：["AAAAACCCCC", "CCCCCAAAAA"]
# 
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        from collections import defaultdict
        helper = defaultdict(int)
        size = len(s)
        res = []
        for i in range(size-9):
            curr = s[i:i+10]
            helper[curr]+=1
            if helper[curr]>1:
                res.append(curr)
        return list(set(res))
# @lc code=end

