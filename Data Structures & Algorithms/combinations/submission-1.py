class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = range(1, n+1)
        path = []
        combs = []
        def dfs(i):
            if len(path) == k:
                combs.append(path[:])
                return
            if i >= n:
                return
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
            dfs(i + 1)
        dfs(0)
        return combs
