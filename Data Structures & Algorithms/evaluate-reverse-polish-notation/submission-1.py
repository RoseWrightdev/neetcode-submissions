class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        ops = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y),
        }
        for token in tokens:
            if token in ops:
                y = stk.pop()
                x = stk.pop()
                stk.append(ops[token](x, y))
            else:
                stk.append(int(token))
        return stk[-1]
