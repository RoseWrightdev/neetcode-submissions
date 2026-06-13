from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False


        count = Counter(nums)
        if count.most_common(1)[0][1] >= 2:
            return True
        else:
            return False