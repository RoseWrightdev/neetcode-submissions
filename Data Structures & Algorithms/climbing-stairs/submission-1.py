class Solution:
    def climbStairs(self, n: int) -> int:
        # if n <= 2:
        #     return n
        # steps = [0] * (n + 1)
        # steps[1], steps[2] = 1, 2
        # for i in range(3, n + 1):
        #     steps[i] = steps[i-1] + steps[i-2]
        # return steps[n]
        memo = {}
        def dfs(i):
            if i >= n:
                return i == n
            if (i + 1) not in memo:
                memo[i + 1] = dfs(i + 1)
            if (i + 2) not in memo:
                memo[i + 2] = dfs(i + 2)
            return memo[i + 1] + memo[i + 2]

        return dfs(0)
