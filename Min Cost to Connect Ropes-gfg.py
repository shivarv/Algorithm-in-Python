import heapq
class Solution:
    def minCost(self, arr):
        # code here
        heapArr = []
        prevOp = 0
        currentOp = 0
        totalCost = 0
        for arrItem in arr:
            heapq.heappush(heapArr, arrItem)
        
        while len(heapArr) > 1:
            first = heapq.heappop(heapArr)
            second = heapq.heappop(heapArr)
            sum = first + second
            heapq.heappush(heapArr, sum)
            totalCost += sum
        return totalCost