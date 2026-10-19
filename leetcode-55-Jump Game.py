class Solution:
    def canJump(self, nums: list[int]) -> bool:
        lastIndexReached = len(nums) -1
        i = len(nums) - 2
        while i >= 0:
            if nums[i] + i >= lastIndexReached:
                lastIndexReached = i
            i -= 1
        return lastIndexReached == 0