class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        def linear_search(arr, num):
            for item in arr:
                if num == item:
                    return True

        if not nums:
            return 0
        
        longest = 1
        curr_longest = 1

        hash_set = set(nums)
        n = len(hash_set)
        
        for num in hash_set:

            if num - 1 in hash_set:
                continue
            
            required = num + 1
            
            while required in hash_set:
                curr_longest += 1
                required += 1
            
            longest = max(curr_longest, longest)
            curr_longest = 1
        
        return longest
