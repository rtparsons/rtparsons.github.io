import pytest


def selection_sort(to_sort):
    if not isinstance(to_sort, list):
        return to_sort

    for i in range(0, len(to_sort)):
        min_index = i
        for j in range(i, len(to_sort)):
            if to_sort[j] < to_sort[min_index]:
                min_index = j
        
        to_sort[i], to_sort[min_index] = to_sort[min_index], to_sort[i]
    
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
def test_selection_sort(input, expected):
    assert selection_sort(input) == expected
