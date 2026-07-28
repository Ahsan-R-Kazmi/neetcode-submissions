class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)

        ans = []

        cutoff = len(nums) / 3


        for num, count in c.items():
            if count > cutoff:
                ans.append(num)

        return ans