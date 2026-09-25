class Solution:
    def singleNumber(self, nums: list[int]) -> int:

        n = len(nums)
        count_map = defaultdict()

        for i in range(n):
            count_map[nums[i]] = count_map.get(nums[i], 0) + 1
        
        for key, value in count_map.items():
            if value == 1:
                return key

        