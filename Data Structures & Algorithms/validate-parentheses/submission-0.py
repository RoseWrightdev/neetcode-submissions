class Solution:
    def isValid(self, s: str) -> bool:
        hm = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        stk = []

        for c in s:
            if c not in hm:
                stk.append(c)                
            elif not stk or stk[-1] != hm[c]:
                return False
            else:
                stk.pop()
        
        return not stk

