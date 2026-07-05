class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def  dfs(i, path, curr):
            if curr == target:
                res.append(path[:])
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if curr + candidates[j] > target:
                    break
                path.append(candidates[j])
                dfs(j + 1, path, curr + candidates[j])
                path.pop()
        dfs(0, [], 0)
        return res

                