import pytest


def double_ended_selection_sort(to_sort):
    if not isinstance(to_sort, list):
        return to_sort

    print(to_sort)
    for i in range(0, len(to_sort)):
        min_index_pos = i
        max_index_pos = len(to_sort) - (i + 1)
        min_index = i
        max_index = len(to_sort) - (i + 1)
        
        if min_index >= max_index:
            return to_sort
        for j in range(min_index, max_index + 1):
            if to_sort[j] < to_sort[min_index]:
                min_index = j
            if to_sort[j] > to_sort[max_index]:
                max_index = j
        
        to_sort[min_index_pos], to_sort[min_index] = to_sort[min_index], to_sort[min_index_pos]
        if max_index == min_index_pos:
            max_index = min_index
        to_sort[max_index_pos], to_sort[max_index] = to_sort[max_index], to_sort[max_index_pos]

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
def test_double_ended_selection_sort(input, expected):
    assert double_ended_selection_sort(input) == expected
