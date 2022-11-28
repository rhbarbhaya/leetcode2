import pytest
from question15.question15 import threeSum

@pytest.mark.parametrize(
    'nums, output',[
        ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
        ([0,1,1], []),
        ([0,0,0], [[0,0,0]],)
    ]
)
def test_threeSum(nums, output):
    assert threeSum(nums) == output