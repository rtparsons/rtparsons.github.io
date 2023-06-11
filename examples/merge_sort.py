import pytest


def merge_sort(to_sort: list):
    if not isinstance(to_sort, list):
        return to_sort
     
    if len(to_sort) < 2:
        return to_sort
    
    mid_point: int = len(to_sort) // 2
    left: list = to_sort[:mid_point]
    right: list = to_sort[mid_point:]

    merge_sort(left)
    merge_sort(right)

    for i in range(len(to_sort)):
        print(to_sort)
        if left and right and left[0] <= right[0]:
            to_sort[i] = left.pop(0)
        elif not right:
            to_sort[i] = left.pop(0)
        else:
            to_sort[i] = right.pop(0)
    
    return to_sort


test_data = [
    (None, None),
    ([], []),
    ([1, 2, 3], [1, 2, 3]),
    ([3, 2, 1], [1, 2, 3]),
    ([-1, -5, -2, -4], [-5, -4, -2, -1]),
    ([0, 1, 0, -3, 999, 0, -1], [-3, -1, 0, 0, 0, 1, 999])
]


@pytest.mark.parametrize("input,expected", test_data)
def test_merge_sort(input, expected):
    assert merge_sort(input) == expected

