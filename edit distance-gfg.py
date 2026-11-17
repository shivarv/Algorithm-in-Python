class Solution:
	def editDistance(self, s1, s2):
		# code here
		len1 = len(s1)
		len2 = len(s2)
		#remember its len2 , len1 for memo
		#len1 is rows, len2 is columns.. so
		memo = [[-1] * (len2 + 1) for _ in range(len1 + 1)]
		return self.editDistanceHelper(s1, s2, len1, len2, memo)
	
	def editDistanceHelper(self, s1, s2, i, j, memo):
	    if i == 0 and j == 0:
	        return 0
	    if i == 0:
	        return j
	    if j == 0:
	        return i
	    if memo[i][j] != -1:
	        return memo[i][j]
	    if s1[i - 1] == s2[j - 1]:
	        memo[i][j] = self.editDistanceHelper(s1, s2, i - 1, j - 1, memo)
	    else:
            memo[i][j] =  1 + min(self.editDistanceHelper(s1, s2, i - 1, j - 1, memo),
                                self.editDistanceHelper(s1, s2, i - 1, j, memo),
                                self.editDistanceHelper(s1, s2, i, j - 1, memo))
	    return  memo[i][j]