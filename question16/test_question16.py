import pytest
from question16.question16 import Solution

solution = Solution()

@pytest.mark.parametrize(
    ('nums, target, output'),[
        ([-1,2,1,-4], 1, 2),
        ([0,0,0], 1, 0),
    ]
)
def test_threeSumClosest(nums, target, output):
    assert solution.threeSumClosest(nums, target) == output