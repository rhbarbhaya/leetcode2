from question8.question8 import Solution
import pytest

solution = Solution()

@pytest.mark.parametrize(
    's, output',[
        ("42", 42),
        ("   -42", -42),
        ("4193 with words", 4193),
        ("words and 987", 0),
        ("+-12", 0)
    ]
)
def test_myAtoi(s, output):
    assert solution.myAtoi(s) == output