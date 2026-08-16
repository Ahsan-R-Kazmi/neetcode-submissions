class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        color_count = [0] * 3

        for num in nums:
            color_count[num] += 1

        k = 0
        for i in range(len(color_count)):

            j = color_count[i]
            while j > 0:
                nums[k] = i
                j -= 1
                k += 1