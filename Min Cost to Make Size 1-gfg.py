class Solution:

    def cost(self, arr: list[int]) -> int:
        minValue = arr[0]
        
        for arrVal in arr:
            if arrVal < minValue:
                minValue = arrVal
        
        return minValue * (len(arr) - 1)
