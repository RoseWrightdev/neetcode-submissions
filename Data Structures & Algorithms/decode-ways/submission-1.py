class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}
        def dfs(i):
            if i == n:
                return 1
            if s[i] == '0':
                return 0 
            if i + 1 not in memo:
                memo[i + 1] =  dfs(i + 1)      
            res = memo[i + 1]
            if i < n - 1:
                if s[i] == '1' or (s[i] == '2' and s[i + 1] < '7'):
                    if i + 2 not in memo:
                        memo[i + 2] =  dfs(i + 2)     
                    res += memo[i + 2]
            return res
        return dfs(0)
                 
            


            