class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        memo = [ [-1] * (len2 + 1) for _ in range (len1 + 1)]
        return self.minDistanceHelper(word1, word2, len1, len2, memo)

    def minDistanceHelper(self, word1: str, word2: str, i: int, j:int, memo:list[list[int]]) -> int:
        if i == 0 and j == 0:
            return 0 
        if i == 0:
            return j
        if j == 0:
            return i
        if memo[i][j] != -1:
            return memo[i][j]
        #same
        if word1[i - 1] == word2[j - 1]:
            memo[i][j] = self.minDistanceHelper(word1, word2, i - 1, j - 1, memo)
        else:
            #replace, #delete move only i, #insert - move only j)
            memo[i][j] = 1 + min(
                self.minDistanceHelper(word1, word2, i - 1, j - 1, memo),
                self.minDistanceHelper(word1, word2, i - 1, j, memo),
                self.minDistanceHelper(word1, word2, i, j - 1, memo))
        return memo[i][j]