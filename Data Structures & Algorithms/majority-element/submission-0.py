class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        c = Counter(nums)

        ans = -1
        vote = 0

        for num, count in c.items():
            if count > vote:
                ans = num
                vote = count
        
        return ans
