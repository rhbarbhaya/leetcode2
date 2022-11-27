from question9.question9 import isPalindrome
import pytest

@pytest.mark.parametrize(
    'x, output',[
        (121, True),
        (-121, False),
        (10, False),
    ]
)
def test_isPalindrome(x, output):
    assert isPalindrome(x) == output
