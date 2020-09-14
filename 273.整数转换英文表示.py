#
# @lc app=leetcode.cn id=273 lang=python3
#
# [273] 整数转换英文表示
#

# @lc code=start
class Solution:
    def numberToWords(self, num: int) -> str:
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        if num==0:
            return "Zero"
        def helper(num):
            if num<20:
                return to19[num-1:num]# list type + avoid 0
            if num<100:
                return [tens[num//10-2]] + helper(num%10)
            if num<1000:
                return helper(num//100) + ["Hundred"] + helper(num%100)
            for p,w in enumerate(["Thousand", "Million", "Billion"], 1):
                if num < 1000**(p+1):
                    return helper(num//(1000**p)) + [w] + helper(num%(1000**p))
        res = " ".join(helper(num))
        return res
# @lc code=end

