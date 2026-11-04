class Solution:
    def knapsack(self, W: int, val: list[int], wt: list[int]) -> int:
        # code here
        #remember if W is 5, then u can carry from 0 - 5..so array is 6
        dp = [[-1] * (W + 1) for _ in range(len(val))]
        return self.knapSackHelper(val, wt, W,0, dp)
        
        
    def knapSackHelper(self, val, wt, capacity,index, dp):
        if index == len(val):
            return 0
        if(dp[index][capacity] != -1):
            return dp[index][capacity]
        take = 0
        if capacity >= wt[index]:
            take = val[index] + self.knapSackHelper(
                val, wt,capacity - wt[index], index +1, dp)
        notTake = self.knapSackHelper(val, wt, 
                capacity, index +1, dp)
        dp[index][capacity] = max(take, notTake)
        return dp[index][capacity]