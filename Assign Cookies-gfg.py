class Solution:
    def maxChildren(self, greed, cookie):
        greed.sort(reverse = True)
        cookie.sort(reverse = True)
        left = 0
        right = len(greed)
        leftCookie = 0
        rightCookie = len(cookie)
        greedPossible = 0
        while (leftCookie < rightCookie):
            while(left < right):
                if(greed[left] <= cookie[leftCookie]):
                    greedPossible += 1
                    left += 1
                    break;
                else:
                    left += 1
            leftCookie += 1
        return greedPossible
        
