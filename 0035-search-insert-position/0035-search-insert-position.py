class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        n = len(nums)
        ans = n
        start = 0
        end = n - 1

        while(start <= end):

            mid = start + (end - start) // 2

            if target <= nums[mid]:
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        
        return ans

        