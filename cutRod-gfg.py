class Solution:
    def cutRod(self, price: list[int]) -> int:
        dp = [ [-1] * (len(price) + 1) for _ in range(len(price) +1)]
        return self.cutRodHelper(price, 0, len(price),  dp)
    
    def cutRodHelper(self, prices:list[int], index, n,  dp) -> int:
        if index >= len(prices) or n == 0:
            return 0
        if dp[index][n] != -1:
            return dp[index][n]
        taken = float('-inf')
        #i can only take if index + 1 <= n, becz index is the array notation
        if index + 1 <= n:
            taken = prices[index] + self.cutRodHelper(prices, index, 
                                n - (index +1), dp)
        notTaken = self.cutRodHelper(prices, index + 1, 
                            n, dp)
        dp[index][n] = max(taken, notTaken)
        return dp[index][n]
        
        
        
class Solution:
    def cutRod(self, price: list[int]) -> int:
        #becz n is the size
        n = len(price)
        dp = [-1] * (n + 1)

        def solve(remaining):
            if remaining == 0:
                return 0

            if dp[remaining] != -1:
                return dp[remaining]

            best = 0

            #becz the problem states that 
            for i in range(remaining):
                best = max(
                    best,
                    price[i] + solve(remaining - (i + 1))
                )

            dp[remaining] = best
            return best

        return solve(n)
