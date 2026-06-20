from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)

        if n > m:
            return False
        
        premu = Counter(s1)
        window = Counter(s2[:n])

        if premu == window:
            return True
        
        for right in range(n, m):
            window[s2[right]] += 1
            left_char = s2[right - n]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
            if premu == window:
                return True
        return False
