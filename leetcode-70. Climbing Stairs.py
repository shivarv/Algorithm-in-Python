class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        current = 1
        numberOfWays = current
        for i in range(2, n + 1):
            numberOfWays = prev + current
            prev = current
            current = numberOfWays
        return numberOfWays
        