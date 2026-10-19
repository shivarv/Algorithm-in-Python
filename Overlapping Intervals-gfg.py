import heapq
class Solution:
	def mergeOverlap(self, arr):
		# Code here
		pq = []
		output = []
        #arr = sorted(arr, key=lambda x: x[0])
        lastItemStart = -1
        lastItemEnd = -1
        for start, end in arr:
            heapq.heappush(pq, (start, end))
        item = heapq.heappop(pq)
        lastItemStart = item[0]
        lastItemEnd = item[1]
        while pq:
            item = heapq.heappop(pq)
            if lastItemEnd >= item[0]:
               lastItemEnd = max(lastItemEnd, item[1])
            else:
                output.append([lastItemStart, lastItemEnd])
                lastItemStart = item[0]
                lastItemEnd = item[1]
        output.append([lastItemStart, lastItemEnd])
        return output
        
#another approach

import heapq
class Solution:
    def mergeOverlap(self, arr):
        arr.sort()
        mergedInterval = []
        mergedInterval.append(arr[0])
        for i in range(1, len(arr)):
            lastItem = mergedInterval[-1]
            currentItem = arr[i]
            if lastItem[1] >= currentItem[0]:
                lastItem[1] = max(lastItem[1], currentItem[1])
            else:
                mergedInterval.append(currentItem)
        return mergedInterval