class Solution:
    def findMin(self, n: int) -> int:
        coins = [1, 2 , 5, 10]
        count = 0
        i = len(coins) - 1
        while i >= 0 and n > 0:
            if n < coins[i]:
               i -= 1
            else:
                count += (n // coins[i])
                n = n % coins[i]
                i -= 1
        return count