class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        answers = []
        def backtrack(ans: List[int], selected: Set[int]):

            nonlocal answers
            if len(ans) == len(nums):
                answers.append(ans[:])
                return
            
            for i, num in enumerate(nums):
                if i not in selected:
                    ans.append(num)
                    selected.add(i)
                    backtrack(ans, selected)
                    ans.pop()
                    selected.remove(i)

        backtrack([], set())
        return answers
