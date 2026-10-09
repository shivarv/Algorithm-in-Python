class Solution:
    def minMaxCandy(self, prices, k):
        # code here
        prices.sort()
        minCount = len(prices) // (k + 1)
        if len(prices) % (k + 1) != 0:
            minCount += 1
        min = sum(prices[0: minCount])
        max = sum(prices[-minCount: ])
        return [min, max]