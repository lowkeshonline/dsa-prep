class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        1. Find the break point element index
        2. find the element greater than the break point element and less than others from right
        3. swap the break point element with adjacent greater element found
        4. now reverse the entire array after the break point to automatically sort the elements

        """

        n = len(nums)
        break_idx = -1

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break_idx = i

                break
                
        if break_idx == -1:
            return nums.reverse()
        
        for j in range(n - 1, -1, -1):
            if nums[j] > nums[break_idx]:
                temp = nums[j]
                nums[j] = nums[break_idx]
                nums[break_idx] = temp

                break
        
        left = break_idx + 1
        right = n - 1

        while(left < right):

            nums[left], nums[right] = nums[right], nums[left]

            left += 1
            right -= 1
        
        return nums

        