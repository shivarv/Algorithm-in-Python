class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        memo = [[-1] * (n + 1) for _ in range(k + 1)]
    
        return self.superEggDropHelper(k, n, memo)

    def superEggDropHelper(self, eggs:int, floors:int, memo) -> int:
        if eggs == 0:
            return float('inf')
        if floors == 0 or floors == 1:
            return floors
        if eggs == 1:
            return floors
        if memo[eggs][floors] != -1:
            return memo[eggs][floors]
        minOutput = float('inf')
        
        for x in range(1, floors + 1):
            broken = self.superEggDropHelper(eggs - 1, x - 1, memo)
            notBroken = self.superEggDropHelper(eggs, floors - x, memo)
            worstCase = 1 + max(broken, notBroken)
            if minOutput > worstCase:
                minOutput = worstCase
        memo[eggs][floors] = minOutput
        return memo[eggs][floors]
        
class Solution:

    def superEggDrop(self, k: int, n: int) -> int:
        memo = [[-1] * (n + 1) for _ in range(k + 1)]
    
        return self.superEggDropHelper(k, n, memo)

    def superEggDropHelper(self, eggs:int, floors:int, memo) -> int:
        if eggs == 0:
            return sys.maxsize
        if floors == 0 or floors == 1:
            return floors
        if eggs == 1:
            return floors
        if memo[eggs][floors] != -1:
            return memo[eggs][floors]
        
        minOutput = sys.maxsize
        low = 1
        high = floors

        while low <= high:
            mid = (low + high) // 2
            broken = self.superEggDropHelper(eggs - 1, mid - 1, memo)
            notBroken = self.superEggDropHelper(eggs, floors - mid, memo)
            worstCase = 1 + max(broken, notBroken)

            if minOutput > worstCase:
                minOutput = worstCase

            if broken == notBroken:
                break
            elif broken < notBroken:
                low = mid + 1
            else:
                high = mid - 1

        memo[eggs][floors] = minOutput
        return memo[eggs][floors]