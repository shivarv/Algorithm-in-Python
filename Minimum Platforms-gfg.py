# logic is simply sort arr and dep , doesnt need to include them 
# loop through length.. inside if arr[i] <= dep[j], increment count
#else decrement count
#assign the max of the current count or the res to the res
class Solution:
    def minPlatform(self, arr: list[int], dep: list[int]) -> int:
        # code here
        arr.sort()
        dep.sort()
        i, j = 0, 0
        n = len(arr)
        #loop through n ,i for arr, j for dep
        res = 0
        count = 0
        while i < n and j < n:
            if arr[i] <= dep[j]:
                i += 1
                count += 1
            else:
                count -= 1
                j += 1
            res = max(res, count)
        return res