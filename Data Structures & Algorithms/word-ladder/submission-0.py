class Solution:
    def ladderLength(self, begin: str, end: str, word_list: List[str]) -> int:
        if begin == end:
            return 0

        word_set = set(word_list)

        q = deque()
        visited = set()

        q.append((begin, 1))
        visited.add(begin)

        while len(q) > 0:
            word, distance = q.popleft()

            if word == end:
                return distance

            for i in range(len(word)):
                c = word[i]

                for j in range(0, 26):
                    new_c = chr(ord("a") + j)
                    if c == new_c:
                        continue

                    new_word = word[:i] + new_c + word[i + 1 :]
                    if new_word in word_set and new_word not in visited:
                        q.append((new_word, distance + 1))
                        visited.add(new_word)

        return 0
