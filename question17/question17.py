from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        res = []
        if len(digits) == 0:
            return res
        def backtrack(k, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return
            for character in mapping[digits[k]]:
                backtrack(k+1, curr+character)
        backtrack(0, '')
        return res
            

solution = Solution()
