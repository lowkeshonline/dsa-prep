class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        new_arr = [0] * n

        k = k % n

        for i in range(n):

            new_idx = (i + k) % n

            new_arr[new_idx] = nums[i]

        nums[:] = new_arr

            
        

                


        

        