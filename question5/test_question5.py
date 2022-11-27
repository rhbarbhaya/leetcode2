import pytest
from question5.question5 import Solution

solution = Solution()

@pytest.mark.parametrize(
    's, output',[
        ('babad', 'bab'),
        ('cbbd', 'bb'),
    ]
)
def test_solution(s, output):
    assert solution.longestPalindrome(s) == output