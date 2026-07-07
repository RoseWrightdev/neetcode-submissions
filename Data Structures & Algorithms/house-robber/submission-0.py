class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i + 1 not in memo:
                memo[i + 1] = dfs(i + 1)
            if i + 2 not in memo:
                memo[i + 2] = dfs(i + 2)
            return max(memo[i + 1], nums[i] + memo[i + 2])
        return dfs(0)