class Solution:
    def search(self, nums: list[int], target: int) -> int:

        n = len(nums)
        start = 0
        end = n - 1
        ans = -1

        while(start <= end):

            mid = start + (end - start) // 2

            if nums[mid] == target:
                ans = mid

            if nums[start] <= nums[mid]:
                if target >= nums[start] and target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target <= nums[end] and target >= nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1

        return ans


        
        