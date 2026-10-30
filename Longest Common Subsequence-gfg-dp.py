#self.lcsCal is import..to declare use self in paramter but when calling use self.methodName but dont pass self
#u can do n+1 , m +1 memo and use m == 0 or n == 0 and lcsCal(s1, s2, m, n , memo)
class Solution:
    def lcs(self, s1, s2):
        m  = len(s1)
        n = len(s2)
        memo = [[-1] * n for _ in range(m)]
        return self.lcsCal(s1, s2, m -1, n -1, memo)

    def lcsCal(self, s1, s2, m, n,memo):
        if(m < 0 or n < 0):
            return 0
        if(memo[m][n] != -1):
            return memo[m][n]
        if(s1[m] == s2[n]):
            memo[m][n] = 1 + self.lcsCal(s1, s2, m - 1, n -1, memo)
            return memo[m][n]
        memo[m][n] = max(self.lcsCal(s1, s2, m, n -1, memo),
                        self.lcsCal(s1, s2, m - 1, n, memo)
                        )
        return memo[m][n]