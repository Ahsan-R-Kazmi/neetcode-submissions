class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left: List[int], right: List[int]) -> List[int]:
            i = 0
            j = 0

            merged = []

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])

            return merged

        def mergesort(nums: List[int]) -> List[int]:

            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2
            left = mergesort(nums[:mid])
            right = mergesort(nums[mid:])

            return merge(left, right)

        return mergesort(nums)
