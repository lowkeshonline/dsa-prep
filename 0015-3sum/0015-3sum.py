class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        n = len(nums)
        # take a set as result to prevent duplicate triplets
        res = set()
        nums.sort()

        # the i should go till the second last element to leave space for inner loop
        for i in range(n - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left , right = i + 1, n - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total == 0:

                    triplets = tuple(sorted([nums[i], nums[left], nums[right]]))
                    res.add(triplets)
                    left += 1
                    right -= 1
                    # if total less than target increase smaller side
                elif total < 0:
                    left += 1
                    # if doesn't greater than target decrease bigger side
                else:
                    right -= 1

        return list(res)
                
            
        
        