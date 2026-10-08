class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        sum = 0
        max_from_left = nums[0]
        n = len(nums)
        min_from_right = [0] * n
        min_from_right[n - 1] = nums[n - 1]
        
        for i in range(n - 2, -1, -1):
            min_from_right[i] = min(
                nums[i],
                min_from_right[i + 1]
            )
        #it excludes 1 index , -1 at end means reverse
        #for i in range(len(nums) - 1, 1, -1):
            
        for i in range(1, len(nums) - 1):
            right_index = len(nums) - 1 - i
            if nums[i] > max_from_left and nums[i] < min_from_right[i + 1]:
                sum += 2
            elif nums[i] > nums[i - 1] and nums[i] < nums[i + 1]:
                sum +=1
            max_from_left = max(max_from_left, nums[i])
        return sum