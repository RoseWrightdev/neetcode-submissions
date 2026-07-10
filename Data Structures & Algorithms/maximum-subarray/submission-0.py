class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = []
        max_sum = float('-inf')
        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += nums[j]
                max_sum = max(max_sum, curr)
        return max_sum