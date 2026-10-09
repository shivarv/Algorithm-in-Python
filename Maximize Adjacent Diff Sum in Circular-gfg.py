class Solution:
    def maxSum(self,arr):
        # code here
        arr.sort();
        
        left = 0
        right = len(arr) - 1
        result = []

        while left <= right:
            result.append(arr[left])
            left += 1

            if left <= right:
                result.append(arr[right])
                right -= 1
        sum = 0
        for i in range(len(result) - 1):
            sum += abs(result[i] - result[i + 1])
        sum += abs(result[0] - result[len(result) - 1])
        return sum