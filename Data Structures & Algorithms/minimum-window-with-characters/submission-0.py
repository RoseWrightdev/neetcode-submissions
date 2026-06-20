from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        counts = Counter(t)
        required = len(counts)
        window = defaultdict(int)

        left, formed = 0, 0
        shortest = float("inf"), None, None

        for right in range(len(s)):
            right_char = s[right]
            window[right_char] += 1

            if right_char in counts and window[right_char] == counts[right_char]:
                formed += 1

            while left <= right and formed == required:
                left_char = s[left]
                dist = right - left + 1

                if dist < shortest[0]:
                    shortest = (dist, left, right)
                
                window[left_char] -= 1

                if left_char in counts and window[left_char] < counts[left_char]:
                    formed -= 1
                left += 1

        return "" if shortest[0] == float("inf") else s[shortest[1]:shortest[2] + 1]
