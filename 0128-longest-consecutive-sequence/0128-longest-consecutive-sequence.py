class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        longest = 1
        streak = 1
        nums.sort()

        # visit every element in the array

        for i in range(1,len(nums)):

            #handle duplicate elements by skipping them
            if nums[i] == nums[i - 1]:
                continue
            #increase current streak if curr num is 1 digit greater than previous
            elif nums[i] == nums[i - 1] + 1:
                streak += 1
            #else bring down the streak again to 1
            else:
                streak = 1
            
            longest = max(streak, longest)
        
        return longest

        