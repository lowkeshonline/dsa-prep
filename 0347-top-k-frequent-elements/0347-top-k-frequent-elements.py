class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #create a frequency hashmap
        count = {}
        freq_list = [[] for i in range(len(nums) + 1)]
        
        for i in nums:
            count[i] = count.get(i,0) + 1

        for num, count in count.items():
            freq_list[count].append(num)

        res = []
        for i in range(len(freq_list) - 1, -1, -1):

            if len(res) == k:
                return res
            
            for n in freq_list[i]:
                res.append(n)
            


        
        