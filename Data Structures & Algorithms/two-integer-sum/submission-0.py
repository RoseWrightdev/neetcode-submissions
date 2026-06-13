class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for index, num in enumerate(nums):
            comp = target - num
            if comp in hm:
                return [hm[comp], index]
            else:
                hm[num] = index
        