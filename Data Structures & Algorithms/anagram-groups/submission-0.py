class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group_dict = defaultdict(list)

        for s in strs:
            c = [0] * 26

            for char in s:
                c[ord(char) - 97] += 1
            
            key = tuple(c)
            group_dict[key].append(s)

        return list(group_dict.values())