from question4.question4 import Solution
import pytest

solution = Solution()

@pytest.mark.parametrize(
    'input1, input2, output',[
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5)
    ]
)
def test_solution(input1, input2, output):
    assert solution.findMedianSortedArrays(input1, input2) == output
    # assert solution.findMedianSortedArrays([1,2], [3,4]) == 2.5
    
if __name__ == "__main__":
    test_solution()