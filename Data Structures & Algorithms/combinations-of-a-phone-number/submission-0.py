class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return  
            for ch in digitToChar[digits[index]]:
                backtrack(index + 1, curr + ch)
        if digits:
            backtrack(0, "")
        return res
