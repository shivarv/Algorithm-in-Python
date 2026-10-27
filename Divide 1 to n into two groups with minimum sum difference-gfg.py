class Solution:
    #here if n is 7 , means 1 - 7 are the numbers
    def findGroup(n) -> list[list[int]]:
        res = [[][]]
        leftSum = 0
        rightSum = 0
        sum = (n * (n + 1)) /2
        half = sum /2
        for i in range(n , 0 , -1):
            if leftSum + i <=  half:
                res[0].append(i)
                leftSum += i
            else:
                res[1].append(i)
                rightSum += i
        return res
        
    cutPoint = findGroup(n)
    for group in res:
        for x in group:
            print(x, end=" ")
        print()
    