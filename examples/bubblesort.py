import pytest


def bubble_sort(to_sort):
    if not isinstance(to_sort, list):
        return to_sort

    for i in range(len(to_sort) - 1, 0, -1):
        has_swap = False
        for j in range(0, i):
            if to_sort[j] > to_sort[j + 1]:
                has_swap = True
                to_sort[j], to_sort[j + 1] = to_sort[j + 1], to_sort[j]

        if not has_swap:
            return to_sort
      
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
def test_bubble_sort(input, expected):
    assert bubble_sort(input) == expected
