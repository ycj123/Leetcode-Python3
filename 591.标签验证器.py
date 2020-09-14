#
# @lc app=leetcode.cn id=591 lang=python3
#
# [591] 标签验证器
#

# @lc code=start
class Solution:
    def isValid(self, code: str) -> bool:
        if(len(code)<7 or code[0]!='<' or code[-1]!='>'):
            return False
        name = []
        i = 0
        while i<len(code):
            if code[i] == '<':
                if code[i+1] == '!':
                    if not name or i+15>=len(code):
                        return False
                    tmp = code[i:i+9]
                    index = code.find(']]>', i+9)
                    if tmp!='<![CDATA[' or index==-1:
                        return False
                    i = index+2
                else:
                    tmp = ''
                    flag = (code[i+1]=='/')
                    i += 1 if flag else 0
                    i+=1
                    while i<len(code) and code[i]!='>':
                        if 'Z'>=code[i]>='A':
                            tmp += code[i]
                        else:
                            return False
                        i+=1
                    if not tmp or len(tmp)>9 or i==len(code):
                        return False
                    if flag:
                        if not name or tmp!=name[-1]:
                            return False
                        name.pop()
                        if not name and i!=len(code)-1:
                            return False
                    else:
                        name.append(tmp)
            i += 1
        return len(name)==0
# @lc code=end

