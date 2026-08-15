class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = -1
        vote = 0
        for num in nums:
            if vote == 0:
                ans = num
                vote +=1
            elif vote > 0:
                if num == ans:
                    vote += 1
                else:
                    vote -= 1

        return ans