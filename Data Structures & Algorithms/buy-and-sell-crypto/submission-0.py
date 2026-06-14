class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        price = 0
        for right in range(1, len(prices)):
            if prices[left] < prices[right]:
                price = max(price, prices[right] - prices[left])
            else:
                left = right
        return price