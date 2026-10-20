class Solution:
    def nthFibonacci(self, n: int) -> int:
        # code here
        if n == 0 or n == 1:
            return n
        output = [0] * n
        output[0] = 1
        output[1] = 1
        for i in range(2, n):
            output[i] = output[i - 1] + output[i - 2]
        return output[n -1]


        # code here
        if n == 0 or n == 1:
            return n
        previous = 0
        current = 1
        output = 0
        for i in range(1, n):
            output = previous + current
            previous = current
            current = output
        return output
