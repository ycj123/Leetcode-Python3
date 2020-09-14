#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = list(map(int, version1.split('.')))
        ver2 = list(map(int, version2.split('.')))
        i = 0
        while i<min(len(ver1), len(ver2)):
            if ver1[i]>ver2[i]:
                return 1
            elif ver1[i]<ver2[i]:
                return -1
            # equal
            i+=1
        if len(ver1)==len(ver2):
            return 0
        elif len(ver1)>len(ver2):
            for j in range(i, len(ver1)):
                if ver1[j]>0:
                    return 1
        else:
            for j in range(i, len(ver2)):
                if ver2[j]>0:
                    return -1
        return 0

# @lc code=end

