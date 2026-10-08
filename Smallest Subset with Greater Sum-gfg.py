class Solution:
    def minSubset(self, arr):
        # code here
        arr.sort(reverse = True)
        sum = 0
        minCount = 0
        remainAmount = 0
        currentSum = 0
        for arrEle in arr:
            sum += arrEle
        currentSum = sum
        for arrEle in arr:
            remainAmount += arrEle
            currentSum -= arrEle
            minCount += 1
            if remainAmount > currentSum :
                break
        return minCount