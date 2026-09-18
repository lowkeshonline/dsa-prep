class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        n = len(nums)

        left = 0
        right = n - 1

        mid = 0

        if (target < nums[0]):
            return 0

        if (target > nums[n - 1]):
            return n
        

        while(left <= right):
            
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            
            elif target > nums[mid]:
                left = mid + 1
            
            elif target < nums[mid]:
                right = mid - 1
        
        
        if (mid < n and nums[mid] > target):
            return mid
        else:
            return mid + 1 





        



        

                
        