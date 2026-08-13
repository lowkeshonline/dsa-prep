class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        #Initialize a hashmap
        last_seen = {}

        for i,num in enumerate(nums):
            #check if num is already in hashmap
            if num in last_seen:
                #if yes get it's previous index and check the distance to current
                if abs(last_seen[num] - i) <= k:
                    return True
            #if not found update the number with it's index
            last_seen[num] = i
        
        return False


        