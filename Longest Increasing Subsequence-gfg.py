class Solution:
    def lis(self, arr):
        # code here
        LIS = [1] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
           for j in range(i +1, len(arr)):
               if arr[i] < arr[j]:
                   LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
