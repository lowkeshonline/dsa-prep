class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        
        positives = []
        negatives = []

        for num in nums:

            if num < 0:
                negatives.append(num)
            else:
                positives.append(num)
                
        p = 0
        n = 0

        for i in range(0,len(nums),2):
            nums[i] = positives.pop(p)
            nums[i + 1] = negatives.pop(n)

        p += 1
        n += 1

        return nums
        
        