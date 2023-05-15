---
layout: post
title:  "Bubble Sort in Python"
date:   2023-05-15 20:00:00 +0000
categories: python algorithms
permalink: /bubble-sort-python/
---

I've always been very focused on building and maintaining large web applications and systems, as such I feel like I skipped over some of the basics early on in my career. Due to this and my curiosity as to how some of the everyday tools we use work, I thought I would take a look at implementing a few of the core basic algorithms. First up bubble sort.

### What is bubble sort?

Bubble sort is a simple sorting algorithm which steps through a list and progressively compares and swaps adjacent elements. A single pass is an iteration over the entire list and many passes are required to completely sort the list (as many passes as items). Due to this, we say that this algorithm has a time complexity of O(n^2).

Here's how it works...

1. Compare the first and second elements. If they are in the wrong order then swap them.
2. Move on to the second and third elements. Again, if they are in the wrong order, swap them.
3. Repeat till you get to the last element. This is a single pass.
4. Go back to step 1. Repeat until the list is sorted. The worst case is that it will take the same number of passes as elements in the list.

In practice, bubble sort is rarely if ever used in real-world applications due to its inefficiencies. Yet due to its relative simplicity vs other sorting algorithms, it is hugely popular as a teaching tool and programming exercise.

### My solution

I took a TTD approach here and wrote a series of tests which I then looked to pass with the resulting implementation. I find this works great for small isolated problems like this where there is a straightforward input and calculated output to test.

One interesting note is that there are 2 simple optimisations to be made over a 'basic' implementation.

1. If a pass over the list is made and no swaps occur, we are done and can exit early.
2. We can reduce the amount of elements we loop over by one each time as after each pass the largest item will end up at the end.

```python
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
```