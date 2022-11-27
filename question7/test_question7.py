from question7.question7 import Solution
import pytest

solution = Solution()

@pytest.mark.parametrize(
    's,output',[
        (123, 321),
        (-123, -321),
        (120, 21),
        (1534236469, 0),
        (-2147483648, 0)
    ]
)
def test_reverse(s, output):
    assert solution.reverse(s) == output
