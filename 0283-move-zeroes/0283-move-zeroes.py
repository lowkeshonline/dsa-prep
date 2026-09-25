class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        new_arr = []

        for i in range(n):
            
            if nums[i] != 0:
                new_arr.append(nums[i])
        
        for j in range(n):

            if nums[j] == 0:
                new_arr.append(nums[j])
        
        nums[:] = new_arr

        return nums
        