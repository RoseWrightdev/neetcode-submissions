class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(index, curr, total):
            if total == target:
                result.append(curr[:])
                return
            if index >= len(nums) or total > target:
                return
            curr.append(nums[index])
            dfs(index, curr, total + nums[index])
            curr.pop()
            dfs(index + 1, curr, total)
        dfs(0, [], 0)
        return result