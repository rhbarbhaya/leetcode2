from question10.question10 import isMatch
import pytest

@pytest.mark.parametrize(
    's, p, output',[
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
    ]
)
def test_isMatch(s, p, output):
    assert isMatch(s, p) == output