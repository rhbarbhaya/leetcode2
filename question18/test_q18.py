from question18.q18 import Solution
import pytest

Solution = Solution()

@pytest.mark.parametrize(
    'nums, target, output',[
        ([1,0,-1,0,-2,2], 0, [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]),
    ]
)
def test_fourSum(nums, target, output):
    assert set(Solution.fourSum(nums, target)) == set(output)