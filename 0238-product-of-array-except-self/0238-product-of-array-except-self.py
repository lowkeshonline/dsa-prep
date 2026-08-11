class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [1] * n

        #initialize prefix as 1
        prefix = 1

        for i in range(n):
            #update prefix with current num element for next step
            res[i] = prefix
            prefix *= nums[i]

        #so now we have the prefix in our result array

        #now as we initiate the postfix with 1
        postfix = 1
        #iterate the array in reverse
        for i in range(n-1, -1, -1):
            #mulitply the res final element with current postfix
            res[i] *= postfix
            #keep updating current postfix with the nums element
            postfix *= nums[i]

        return res