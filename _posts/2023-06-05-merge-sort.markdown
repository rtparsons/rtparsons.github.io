---
layout: post
title:  "Merge Sort in Python"
date:   2023-06-05 00:00:00 +0000
categories: python algorithms
permalink: /merge-sort/
---

Third in my series of dives into sorting algorithms is merge sort. Please see [bubble sort](/bubble-sort-python/) and [selection sort](/selection-sort/) for my previous entries.


### Example

```python
import pytest


def merge_sort(to_sort: list):
    if not isinstance(to_sort, list):
        return to_sort
     
    if len(to_sort) < 2:
        return to_sort
    
    mid_point: int = len(to_sort) // 2

    left: list = to_sort[:mid_point]
    merge_sort(left)

    right: list = to_sort[mid_point:]
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
```


### What is merge sort

Merge sort is a comparison-based sorting algorithm that follows the divide and conquer strategy. It divides the unsorted list into 2 halves, and then recursively splits those halves again until they can be split not further. Then it works its way back up the list, sorting the results of re-combining the lists as it goes.

I was keen to dig into merge sort as unlike bubble and selection sort, it is a sorting algorithm with real-world application. It has a time complexity of O(n ∗ log n), and a space complexity of O(n). Much improved on the O(n^2) of bubble and selection sort!

In fact, it forms the basis for timsort which is a popular sorting algorithm which is used by many languages base libraries such as Python and Java.
