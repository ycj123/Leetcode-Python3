#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        helper = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        for i in s:
            if i not in helper:#left 
                stack.append(i)
            else:
                if stack and stack[-1] == helper[i]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
# @lc code=end

