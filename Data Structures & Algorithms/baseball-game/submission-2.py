class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record_stack: List[int] = []
        
        for op in ops:
            if op == '+':
                a = record_stack[-1]
                b = record_stack[-2]
                
                record_stack.append(a + b)
            elif op == 'D':
                a = record_stack[-1] * 2
                record_stack.append(a)
            elif op == 'C':
                record_stack.pop(-1)
            else:
                record_stack.append(int(op))
        
        return sum(record_stack)