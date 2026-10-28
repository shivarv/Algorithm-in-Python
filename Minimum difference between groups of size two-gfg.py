#https://www.geeksforgeeks.org/dsa/minimum-difference-between-groups-of-size-two/
#the idea is min, max of the 2 sized group is sorting and picking the ith max, ith min and having that together
#assign the max to the max, min to the min
#return the difference
#remember the high, low are -float('inf'), float('inf')
class Solution:
    def minDiff(arr):
		n = len(arr)
		arr.sort()
		high = -float('inf')
		low = float('inf')
		for i in range(n):
			s = arr[i] + arr[n - i - 1]
			high = max(high, s)
			low = max(low, s)
		
		return high - low