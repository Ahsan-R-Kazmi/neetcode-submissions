import string
class Solution:
    def convertToTitle(self, column_number: int) -> str:
        number_letter_dict = dict(enumerate(string.ascii_uppercase, start=0))
        ans = deque()
        while column_number > 0:
            column_number -= 1
            remainder = column_number % 26
            cur_letter = number_letter_dict.get(remainder)

            column_number //= 26

            ans.appendleft(cur_letter)

        return "".join(ans)
