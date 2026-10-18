class Solution:
    def activitySelection(self, start: list[int], finish: list[int]) -> int:
        #code here
        sfList = sorted(zip(start, finish), key = lambda x: x[1])
        lastFinish = -1
        activitiesCount = 0
        for s, f in sfList:
            if(s > lastFinish):
                activitiesCount += 1
                lastFinish = f
        return activitiesCount
        
        
#steps:
#sort the items in finish ascending
#take the least finish item
#go by the order of least finish time , choose any start item which has start time > currentleast finishtime
#remember heappqRef sorts it by finish[i] in this example by default and creates a tupple there
import heapq
class Solution:
    def activitySelection(self, start: list[int], finish: list[int]) -> int:
        #code here
        heapqRef = []
        for i in range(len(start)):
            heapq.heappush(heapqRef, (finish[i], start[i]))
        activityCount = 0
        lastEarlyFinish = -1
        while heapqRef:
            item = heapq.heappop(heapqRef)
            if(lastEarlyFinish < item[1]):
                lastEarlyFinish = item[0]
                activityCount += 1
        return activityCount