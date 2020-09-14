#
# @lc app=leetcode.cn id=722 lang=python3
#
# [722] 删除注释
#

# @lc code=start
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        s = '\n'.join(source) + '\n'
        i = 1
        end = len(s)
        res = ''
        while i < end:
            curr = s[i-1] + s[i]
            if curr == '//':
                index = s.find('\n', i+1)
                i = index + 1
            elif curr == '/*':
                index = s.find('*/', i+1)
                i = index + 3
            else:
                res += s[i-1]
                i+=1
        return list(filter(len, res.split('\n')))
# @lc code=end

