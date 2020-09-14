#
# @lc app=leetcode.cn id=443 lang=python3
#
# [443] 压缩字符串
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        #double pointer
        curr = 0
        index = 0
        length = len(chars)
        while curr<length:
            i = curr + 1
            while i<length and chars[i]==chars[curr]:
                i+=1
            if i-curr>1:
                number = str(i-curr)
                chars[index] = chars[curr]
                index += 1
                for c in number:
                    chars[index] = c
                    index += 1
            else:
                chars[index] = chars[curr]
                index += 1
            curr = i
        return index
# @lc code=end

