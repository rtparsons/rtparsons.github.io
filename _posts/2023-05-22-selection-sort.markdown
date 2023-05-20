---
layout: post
title:  "Selection Sort in Python"
date:   2023-05-22 00:00:00 +0000
categories: python algorithms
permalink: /selection-sort/
---

Second in my series of dives into sorting algorithms is selection sort. After [/bubble-sort-python/](bubble sort), I wanted to pick another fairly basic algorithm to implement and see if I could optimize it a little further.

### What is selection sort

Selection sort is a simple comparison-based sorting algorithm. It works by repeatedly finding the minimum element from the unsorted portion of the list and swapping it with the first known unsorted element. In its most basic form, it has a time complexity of O(n^2), making it insufficient for real-world application.

Here's how it works...

1. Take the first unsorted element and take that as the minimum
2. Loop through the rest of the unsorted elements, and compare these to the current minimum
3. At the end of the loop, swap the minimum element found with the first unsorted element.
4. Go back to 1, adjusting for the fact that one more element is now sorted. Repeat until we have no more unsorted elements.

### My solution

```python
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
```

### Double selection sort

What jumped out at me whilst implementing this was the fact that the entire algorithm was built around finding just the minimum element and swapping that. Why not track the maximum element too, and do the same at both ends of the list?

```python
import pytest


def double_selection_sort(to_sort):
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
def test_double_selection_sort(input, expected):
    assert double_selection_sort(input) == expected
```

I did some reading after implementing this and discovered that this method is called double selection sort, bidirectional selection sort or shaker sort. It offers a slight improvement over selection sort, although it's still considered O(n^2) time complexity. Unfortunately, I didn't invent the next big sorting improvement this time around...
