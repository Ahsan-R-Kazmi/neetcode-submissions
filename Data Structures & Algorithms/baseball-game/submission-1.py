class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans_list: list[int] = []

        for operation in operations:
            
            if operation.lstrip('-').isnumeric():
                ans_list.append(int(operation))
            else:
                match operation:
                    case '+':
                        a = ans_list[-1]
                        b = ans_list[-2]

                        ans_list.append(a + b)
                    case 'D':
                        ans_list.append(ans_list[-1] * 2)
                    case 'C':
                        ans_list.pop()
                    case _:
                        ValueError('Unexpected operation')

        return sum(ans_list)