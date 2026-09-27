class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        for i in range(n):

            minimum = i

            for j in range(i + 1,n):

                if nums[j] < nums[minimum]:
                    minimum = j
            
            temp = nums[minimum]
            nums[minimum] = nums[i]
            nums[i] = temp

        