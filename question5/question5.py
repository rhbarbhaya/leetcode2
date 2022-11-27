class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            if s[i:] == s[i::-1]:
                print(s[i:])
                return s[i:]