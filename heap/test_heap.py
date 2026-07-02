from heap import Heaps
import pytest

heap1 = Heaps(5)
heap1.push(1)
heap1.push(2)
heap1.push(10)
heap1.push(20)
heap1.push(21)
heap1.push(15)
heap1.push(100)
heap1.display()
print()

heap1.delete_peak()
heap1.display()
print()
heap1.delete_peak()
heap1.display()


def test_single_push():
    h = Heaps(2)
    h.push(10)
    assert h.heap == [10]


def test_push_multiple_binary():
    h = Heaps(2)
    for val in [10, 20, 5, 30]:
        h.push(val)
    assert max(h.heap) == h.heap[0]


def test_push_multiple_ternary():
    h = Heaps(3)
    for val in [5, 15, 10, 20, 3]:
        h.push(val)
    assert max(h.heap) == h.heap[0]


def test_delete_peak():
    h = Heaps(2)
    for val in [10, 15, 5, 20]:
        h.push(val)
    peak = h.heap[0]
    h.delete_peak()
    assert peak not in h.heap
    if len(h.heap) > 1:
        assert max(h.heap) == h.heap[0]


def test_delete_peak_empty():
    h = Heaps(2)
    h.delete_peak()
    assert h.heap == []


@pytest.mark.parametrize("values, arity", [
    ([50, 40, 30, 20, 10], 2),
    ([5, 10, 20, 30, 40], 3),
    ([1, 100, 50, 25, 75, 60], 4)
])
def test_heap_property(values, arity):
    h = Heaps(arity)
    for val in values:
        h.push(val)
    for i in range(1, len(h.heap)):
        for j in range(1, arity + 1):
            child = i * arity + j
            if child < len(h.heap):
                assert h.heap[i] >= h.heap[child]
