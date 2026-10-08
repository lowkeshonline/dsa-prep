class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        def lower_bound(nums, target):
            start = 0
            end = len(nums) - 1
            ans = -1

            while(start <= end):

                mid = start + (end - start) // 2

                if target <= nums[mid]:
                    ans = mid
                    end = mid - 1
                else:
                    start = mid + 1
            
            return ans

        def upper_bound(nums, target):
            
            start = 0
            end = len(nums) - 1
            ans = len(nums)

            while(start <= end):
                mid = start + (end - start) // 2

                if target < nums[mid]:
                    ans = mid
                    end = mid - 1
                else:
                    start = mid + 1
            
            return ans

        first = lower_bound(nums, target)

        if first == -1 or nums[first] != target:
            return [-1,-1]
        else:
            return [first, upper_bound(nums, target) - 1]

