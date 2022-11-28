from question20.q20 import Solution
import pytest

Solution = Solution()

@pytest.mark.parametrize(
    's, output',[
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        (")[", False)
    ]
)
def test_isValid(s, output):
    assert Solution.isValid(s) == output
