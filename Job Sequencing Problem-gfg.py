# Create a list of (deadline, profit) tuples and sort by deadline ascending.
# Create an empty min-heap (pq) to store selected job profits.
# Loop through each job:
#   If job[0] > len(pq), there is room to select another job.
#       Push job[1] (profit) into the min-heap using heappush().
#   Else if pq is not empty and pq[0] < job[1]:
#       Remove the minimum profit using heappop() and push the current profit.
#   Otherwise, skip the job.
# Finally, pop all heap elements to count selected jobs and sum their profits.
# job[0] = deadline | job[1] = profit | pq[0] = minimum selected profit
# Time: O(n log n) | Space: O(n)

import heapq
class Solution:
    def jobSequencing(self, deadline, profit):
        n = len(deadline)
        output = [0, 0]
        jobs = [(deadline[i], profit[i]) for i in range(n)]
        jobs.sort();
        pq = []
        for job in jobs:
            if job[0] > len(pq): # we checking if deadline is > pq's size
                heapq.heappush(pq, job[1])
            elif pq and pq[0] < job[1]: #we comparing the profit
                heapq.heappop(pq)
                heapq.heappush(pq, job[1])
        while pq:
            output[1] += heapq.heappop(pq)
            output[0] += 1
        return output