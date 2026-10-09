class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxAdjElementValue = 0
        for i in range(len(nums) - 1):
            if abs(nums[i] - nums[i + 1]) > maxAdjElementValue:
                maxAdjElementValue = abs(nums[i] - nums[i + 1])
        if abs(nums[0] - nums[len(nums) -1]) > maxAdjElementValue:
                maxAdjElementValue = abs(nums[0] - nums[len(nums) -1])
        return maxAdjElementValue
        