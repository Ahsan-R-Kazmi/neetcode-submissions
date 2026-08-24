class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        answers = []
        seen_answers = set()

        def backtrack(ans: List[int], used_indices: Set[int]):

            if len(ans) == len(nums) and tuple(ans) not in seen_answers:
                answers.append(ans[:])
                seen_answers.add(tuple(ans))

            for i, num in enumerate(nums):
                if i not in used_indices:
                    ans.append(num)
                    used_indices.add(i)
                    backtrack(ans, used_indices)
                    ans.pop()
                    used_indices.remove(i)

        backtrack([], set())
        return answers