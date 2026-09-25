class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:

        n = len(nums)

        maximum = 0
        curr_maximum = 0

        for i in range(n):
            if nums[i] == 1:
                curr_maximum += 1
                maximum = max(curr_maximum, maximum)
            else:
                curr_maximum = 0

        
        return maximum


        