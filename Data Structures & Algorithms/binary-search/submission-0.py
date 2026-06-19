class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums)-1
        while left <= right:
            mid = (right + left) // 2
            curr = nums[mid]
            if curr > target:
                right = mid - 1
            elif curr < target:
                left = mid + 1
            else:
                return mid

        return -1