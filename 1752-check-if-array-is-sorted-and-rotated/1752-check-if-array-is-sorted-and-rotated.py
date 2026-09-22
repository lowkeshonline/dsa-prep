class Solution:
    def check(self, nums: list[int]) -> bool:

        breaks = 0

        for i in range(len(nums)):
            
            if nums[(i + 1) % len(nums)] < nums[i]: breaks += 1
            
        return breaks <= 1
        