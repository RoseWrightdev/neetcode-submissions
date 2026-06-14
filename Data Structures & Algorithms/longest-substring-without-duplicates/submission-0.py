class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        chars = set()
        for right in range(len(s)):
            while left < right and s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            longest = max(longest, right - left + 1)
        return longest