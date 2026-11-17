class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)] 
        return self.uniquePathsHelper(m, n, 0, 0, memo);

    def uniquePathsHelper(self, m: int, n: int, currentM: int, currentN: int, memo: List[List[int]] ) -> int:
        if currentM == m - 1 and currentN == n - 1:
            return 1
        if currentM >= m or currentN >= n:
            return 0
        if memo[currentM][currentN] != -1:
            return memo[currentM][currentN]
        right = self.uniquePathsHelper(m, n, currentM, currentN + 1, memo)
        bottom = self.uniquePathsHelper(m, n, currentM + 1, currentN, memo)
        memo[currentM][currentN] = right + bottom
        return memo[currentM][currentN]
        
        