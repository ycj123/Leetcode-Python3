#
# @lc app=leetcode.cn id=365 lang=python3
#
# [365] 水壶问题
#

# @lc code=start
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x+y < z:
            return False
        if x==0 or y==0:
            return z==0 or z==x+y
        def gcd(a, b):
            if a < b:
                return gcd(b, a)
            return b if a%b==0 else gcd(a%b, b)# no [][]
        return z%gcd(x,y)==0
# @lc code=end

