class Solution:
    def buyMaximumProducts(self, k: int, prices: list[int]) -> int:
        maxPurchase = 0
        currentK = k
        pricesMap = {}
        for i in range(len(prices)):
            if prices[i] not in pricesMap:
                    pricesMap[prices[i]] = []
            pricesMap[prices[i]].append( i + 1)
        prices.sort()
        for i in range(len(prices)):
            j = 1
            while( prices[i] <= currentK and j <= pricesMap[prices[i]][0]):
                currentK -= prices[i]
                maxPurchase += 1
                j += 1
            pricesMap[prices[i]].pop(0)
            if len(pricesMap[prices[i]]) == 0:
                del pricesMap[prices[i]]
        return maxPurchase



#better algo

class Solution:
    def buyMaximumProducts(self, k: int, prices: list[int]) -> int:
        products = []

        for i in range(len(prices)):
            products.append((prices[i], i + 1))

        products.sort()

        maxPurchase = 0

        for price, quantity in products:
            canBuy = min(quantity, k // price)

            maxPurchase += canBuy
            k -= canBuy * price

            if k == 0:
                break

        return maxPurchase        
