class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        n = len(nums)
        hash_map = {}
        maximum = 0

        for i in range(n):
            hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
        
        for key,value in hash_map.items():
            if value > (n / 2) and value > maximum:
                maximum = key
        
        return maximum


        