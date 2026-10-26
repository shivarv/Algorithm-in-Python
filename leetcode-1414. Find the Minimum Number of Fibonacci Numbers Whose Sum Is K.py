class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib =[]
        fib.append(1)
        fib.append(1)
        count = 0
        while(fib[-1] < k) :
            fib.append(fib[-1] + fib[-2])
       
        while (k > 0):
            for i in range(len(fib) -1 , -1, -1):
                if(k >= fib[i]):
                    k = k - fib[i]
                    count += 1
        return count