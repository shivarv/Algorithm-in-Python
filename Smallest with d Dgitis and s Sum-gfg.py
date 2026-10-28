class Solution:

    def smallestNumber(self, s: int, d: int) -> str:
        # code here 
        output = [0] * d
        output[0] = 1
        smallestNum = 0
        s -= 1
        for i in range(d -1, 0, -1):
            balance = min(s, 9)
            output[i] = balance
            s = s - balance
        output[0] += s
        if output[0] > 9:
            return str(-1)
        
        for num in output:
            smallestNum *= 10
            smallestNum += num
        return str(smallestNum)