class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        output: int = -1
        dp = [ [-1] * (amount + 1) for _ in range(len(coins))]
        output = self.coinChangeHelper(coins, amount, 0, dp)
        return -1 if output == float('inf') else output

    def coinChangeHelper(self, coins: list[int], amount: int, index, 
                                dp: list[list[int]]) -> int:
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')
        if index >= len(coins):
            return float('inf')
        if dp[index][amount] != -1:
            return dp[index][amount]
        taken = float('inf')
        if coins[index] <= amount:
            taken = 1 + self.coinChangeHelper(coins, amount - coins[index],
                index,dp
            )
        notTaken = self.coinChangeHelper(coins, amount, 
                index + 1, dp
            )
        dp[index][amount] =  min(taken, notTaken)
        return dp[index][amount]