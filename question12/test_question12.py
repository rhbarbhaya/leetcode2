from question12.question12 import intToRoman
import pytest

@pytest.mark.parametrize(
    'num, output',[
        (3, 'III'),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
    ]
)
def test_intToRoman(num, output):
    assert intToRoman(num) == output