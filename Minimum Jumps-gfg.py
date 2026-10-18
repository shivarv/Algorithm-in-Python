class Solution:
    def minJumps(self, arr: list[int]) -> int:
        # code here
        left , right = 0,0
        jump = 0
        n = len(arr)
        #important note: if the n is 0 or 1 , 
        #the first step is when u reach end, so no jump
        if(n <= 1):
            return 0
        #the loop ends at right >= n - 1
        #it gotta be n - 1 before it ends when right == n - 1 or more
        while right < n - 1:
            farthest = 0
            #remember right + 1 becz range goes till n - 1
            for i in range(left, right + 1):
                farthest = max(farthest , arr[i] + i)
            #means we couldnt hit more than right by the iteration
            # so no more jump possibility, so -1
            if farthest <= right:
                return -1
            left = right + 1
            right = farthest
            jump += 1
        return jump
                