class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        prevMap = {0:1}
        ans = 0
        curr_sum = 0

        for i in range(n):

            curr_sum += nums[i]

            complement = curr_sum - k

            if complement in prevMap:
                ans += prevMap[complement]
            
            prevMap[curr_sum] = prevMap.get(curr_sum, 0) + 1
        
        return ans


        