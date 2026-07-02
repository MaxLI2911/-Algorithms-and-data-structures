import pytest
import random
from src.sort_algorithms import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort

test_cases = [
    [],
    [1],
    [5, 2, 9, 1, 5, 6],
    [3, 3, 4, 1, 5, -9, 2],
    [10] * 10,
    list(range(100, 0, -1)),
    [random.randint(-1000, 1000) for _ in range(100)]
]


@pytest.mark.parametrize("case", test_cases)
def test_bubble_sort(case):
    assert bubble_sort(case) == sorted(case)


@pytest.mark.parametrize("case", test_cases)
def test_selection_sort(case):
    assert selection_sort(case) == sorted(case)


@pytest.mark.parametrize("case", test_cases)
def test_insertion_sort(case):
    assert insertion_sort(case) == sorted(case)


@pytest.mark.parametrize("case", test_cases)
def test_merge_sort(case):
    assert merge_sort(case) == sorted(case)


@pytest.mark.parametrize("case", test_cases)
def test_quick_sort(case):
    assert quick_sort(case) == sorted(case)
