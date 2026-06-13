class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # result = []
        # for index, num in enumerate(nums):
        #     start = nums[:index]
        #     end = nums[index + 1:]
        #     result.append(math.prod(start + end))
        # return result
        n = len(nums)
        result = [0] * n
        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = suffix[-1] = 1
        for i in range(1, n): # get prefixes
            prefix[i] = nums[i - 1] * prefix[i - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]
        for i in range(n):
            result[i] = prefix[i] * suffix[i]
        return result
