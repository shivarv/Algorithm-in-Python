class Solution:
    memCache = []
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        Solution.memCache = [[-1] * len2 for _ in range(len1)]
        return self.longestCommononSubsequenceHelper(text1, text2, len1 -1, len2 -1)

    def longestCommononSubsequenceHelper(self, text1: str, text2: str,
                                        m: int, n: int):
        if m < 0 or n < 0:
            return 0
        if Solution.memCache[m][n] != -1:
            return Solution.memCache[m][n]
        if text1[m] == text2[n]:  
            Solution.memCache[m][n] = 1 + self.longestCommononSubsequenceHelper(text1, text2,
                m -1, n -1)
            return Solution.memCache[m][n]
        Solution.memCache[m][n] = max(self.longestCommononSubsequenceHelper(text1, text2,
                m -1, n), self.longestCommononSubsequenceHelper(text1, text2,
                m, n -1))
        return Solution.memCache[m][n]