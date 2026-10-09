class Solution:
    def maxEqualSum(self, s1: list[int], s2: list[int], s3: list[int]) -> int:
        # code here
        s1HashMap = {}
        s2HashMap = {}
        s3HashMap = {}
        
        output = 0
        currentItemSum = 0
        i = 0
        for item in reversed(s1):
            currentItemSum += item
            s1HashMap[currentItemSum] = len(s1) - i
        currentItemSum = 0
        for item in reversed(s2):
            currentItemSum += item
            s2HashMap[currentItemSum] = len(s2) - i
        currentItemSum = 0
        for item in reversed(s3):
            currentItemSum += item
            s3HashMap[currentItemSum] = len(s3) - i
        
        for sum_val in reversed(list(s1HashMap.keys())):
                    if sum_val in s2HashMap and sum_val in s3HashMap:
                        return sum_val
        return 0
        

#more clean approach

#in gfg problem s1 = [3, 2, 1, 1, 1], s2 = [4, 3, 2], s3 = [2, 5, 4, 1] this is the stack..but the index[0] is 3, not 1 ..
#the array looks skewed here, thats why sum1 -= s1[i] works.. essentially it gotta be s1.pop()
def maxEqualSum(self, s1: list[int], s2: list[int], s3: list[int]) -> int:
        sum1, sum2, sum3 = sum(s1), sum(s2), sum(s3)
        i, j, k = 0, 0, 0
        n1, n2, n3 = len(s1), len(s2), len(s3)

        # Loop until all three sums are equal or any stack becomes empty
        while i < n1 and j < n2 and k < n3:
            # If all three sums match, we found the maximum equal sum
            if sum1 == sum2 == sum3:
                return sum1

            # Greedily pop the top item from the stack with the largest sum
            if sum1 >= sum2 and sum1 >= sum3:
                sum1 -= s1[i] 
                i += 1
            elif sum2 >= sum1 and sum2 >= sum3:
                sum2 -= s2[j]
                j += 1
            else:
                sum3 -= s3[k]
                k += 1

        return 0