from question6.question6 import convert
import pytest

@pytest.mark.parametrize(
    's, rowNumber, output',[
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A"),
    ]
)
def test_convert(s, rowNumber, output):
    assert convert(s, rowNumber) == output