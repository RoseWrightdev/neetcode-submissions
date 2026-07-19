class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i, path):
            if i == len(nums):
                return 1 if path == target else 0
            if (i, path) in dp:
                return dp[(i, path)]
            add = dfs(i + 1, path + nums[i])
            sub = dfs(i + 1, path - nums[i])
            dp[(i, path)] = add + sub
            return add + sub
        return dfs(0, 0)
                