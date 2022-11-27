from question14.question14 import longestCommonPrefix
import pytest

@pytest.mark.parametrize(
    'strs, output',[
        (["flower","flow","flight"], 'fl'),
        (["dog","racecar","car"], ""),
        (['flower'], 'flower')
    ]
)
def test_longestCommonPrefix(strs, output):
    assert longestCommonPrefix(strs) == output
