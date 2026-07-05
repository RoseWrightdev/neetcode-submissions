class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def is_palindrome(s):
            left, right = 0, len(s)-1
            while left < right:
                if s[left] != s[right]:
                    return False
                left, right = left + 1, right - 1
            return True

        def dfs(i, path):
            if i == len(s):
                res.append(path[:])
                return
            for j in range(i, len(s)):
                if is_palindrome(s[i:j+1]):
                    path.append(s[i:j+1])
                    dfs(j + 1, path)
                    path.pop()
            
        dfs(0, [])
        return res
        