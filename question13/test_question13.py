from question13.question13 import romanToInt
import pytest

@pytest.mark.parametrize(
    's, output',[
        ('III', 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
    ]
)
def test_romanToInt(s, output):
    assert romanToInt(s) == output