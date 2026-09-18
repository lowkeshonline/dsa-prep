class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        n = len(nums)

        left = 0
        right = n - 1

        mid = 0


        while(left <= right):
            
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            
            elif target > nums[mid]:
                left = mid + 1
            
            elif target < nums[mid]:
                right = mid - 1
        
        
        return mid if (mid < n and nums[mid] > target) else mid + 1 





        



        

                
        