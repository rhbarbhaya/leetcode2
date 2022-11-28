import pytest
from question17.question17 import Solution

Solution = Solution()

@pytest.mark.parametrize(
    'digit, output',[
        ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
        ("", []),
        ("2", ["a","b","c"]),
    ]
)
def test_letterCombinations(digit, output):
    assert Solution.letterCombinations(digit) == output
