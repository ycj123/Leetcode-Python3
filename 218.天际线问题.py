#
# @lc app=leetcode.cn id=218 lang=python3
#
# [218] 天际线问题
#

# @lc code=start
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        #swape line
        heap = [0]
        import heapq
        helper = []
        for b in buildings:
            helper.append([b[0], -b[2]])
            helper.append([b[1], b[2]])
        helper.sort()
        pre = 0
        curr = 0
        res = []
        from collections import defaultdict
        d = defaultdict(int)
        for wall in helper:
            if wall[1]<0:
                heapq.heappush(heap, wall[1])
            else:
                d[wall[1]] += 1
            while heap and -heap[0] in d:
                t = -heap[0]
                heapq.heappop(heap)
                d[t] -= 1
                if d[t]==0:
                    d.pop(t)
            curr = -heap[0]
            if curr!=pre:
                res.append([wall[0], curr])
                pre = curr
        return res
# @lc code=end

