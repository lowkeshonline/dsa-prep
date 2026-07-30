class Solution:
    def maxArea(self, height: List[int]) -> int:

        res = 0
        left = 0
        right = len(height) - 1

        while left < right:

            area = (right - left) * min(height[left], height[right])

            res = max(res,area)

            if height[left] > height[right]:
                right -= 1
            elif height[right] > height[left]:
                left += 1
            else:
                left += 1
        
        return res
        