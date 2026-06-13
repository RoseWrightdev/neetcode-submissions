class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for index, num in enumerate(nums):
            start = nums[:index]
            end = nums[index + 1:]
            result.append(math.prod(start + end))
        return result