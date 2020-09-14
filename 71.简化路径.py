#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        for p in path:
            if p=='..':
                if stack:
                    stack.pop()
            elif p and p!='.':
                stack.append(p)
        return '/' + '/'.join(stack)
# @lc code=end

