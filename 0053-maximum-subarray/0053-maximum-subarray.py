class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        maximum = float('-inf')
        curr_sum = 0

        for i in range(len(nums)):
            
            curr_sum = max(nums[i], curr_sum + nums[i])
            maximum = max(maximum, curr_sum)
  
        return maximum



            