class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        """
        Brute force : Write two nested loops. Check each element with every other elements. If it add upto target and not same index return the indices

        Better Approach : Take the complement and store the value as key and index as hash. Check if the complement already exists in the array with index. 
        """

        hash_map = {}

        for idx,val in enumerate(nums):

            complement = target - nums[idx]

            if complement in hash_map:

                return [hash_map[complement], idx]
            
            hash_map[val] = idx

        


        