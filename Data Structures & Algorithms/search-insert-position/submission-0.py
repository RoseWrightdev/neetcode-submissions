class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary(l, r):
            if l > r:
                return l
            mid = (l + r) // 2
            if nums[mid] > target:
                return binary(l, mid - 1)
            elif nums[mid] < target:
                return binary(mid + 1, r)
            else:
                return mid
        return binary(0, len(nums) - 1)