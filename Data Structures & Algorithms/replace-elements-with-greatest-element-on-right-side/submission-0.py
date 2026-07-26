class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        max_element = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            cur_element = arr[i]
            arr[i] = max_element
            max_element = max(max_element, cur_element)

        arr[-1] = -1
        return arr