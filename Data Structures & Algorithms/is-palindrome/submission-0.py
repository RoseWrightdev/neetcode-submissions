class Solution:
    def isPalindrome(self, s: str) -> bool:
        buff = []
        for c in s:
            if c.isalnum():
                buff.append(c)
        s = ''.join(buff).lower()
        
        reverse = []
        for i in range(len(s) - 1, -1, -1):
            reverse.append(s[i])
        return s == ''.join(reverse)

        