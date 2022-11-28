class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            '}': '{',
            ')': '(',
            ']': '[',
        }
        res = [""]
        for i in range(len(s)):
            if s[i] in mapping.values():
                res.append(s[i])
            elif mapping[s[i]] == res[-1]:
                res.pop()
            else:
                return False
        if len(res) > 1:
            return False
        else:
            return True
